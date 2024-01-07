#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
#define MAX_CUMLE_UZUNLUGU 1000
#define MAX_KELIME_UZUNLUGU 100
// Ekonomi ve Teknoloji ile alakali 2 adet siniftan cumle verilerimiz var.Bunlar ayri ayri txt dosyalarinda.

void remove_punctations(const char*, const char*); //Txt dosyamizdaki tum noktalama isaretlerinden kurtulmak icin.

void remove_newline(char *); //Dosyadan okudugumuz her satirin sonundaki \n karakterinden kurtulmak ve sonuna '\0' eklemek icin. (cumle cumle ayirmaya yarayacak.)

void tokenize_and_store_unique_words(char *cumle, char ***kelimeler, int *kelime_sayisi); /* Tum farklı kelimelerden sozluk olusturmamiza yarayacak fonksiyon--
cumleleri BOSLUK karakterine gore ayirir ve sadece FARKLI karakterleri eklememize olanak saglar. Ayrica kelime sayisini takip eder.
*/
void merge_file(const char *dosya1, const char *dosya2, const char *birlesik_dosya); //Sozluk olustururken iki farkli sinifin verilerini bir araya topluyorum.

int compare_strings(const void *a, const void *b); //qsort fonksiyonunda kullanmak icin yapilmis bir fonksiyon.

typedef struct{ //SOZLUK.
    char **sozluk;
    int kelime_sayisi;
}DICTIONARY;

typedef struct{ //metin verilerini cumle cumle ayrilmis versiyonu.
    char **cumleler;
    int cumle_sayisi;
}SENTENCES;

void seperate_sentences(const char *dosyaAdi, SENTENCES *sentences); //metin verilerimizin oldugu dosyadan metin okuma ve metni cumle cumle ayirma amaciyla kullanilan fonksiyon.

typedef struct{ //hot vectorlerimizi rahat etiketleyebilmek icin struct olarak tutacagiz
    int *hot_vector;
    int label;
}HOT_VECTOR;


int benzer_mi(const char *str1,const char *str2){
/*Eger bir kelime ile diger kelime arasinda 6 harften daha fazla benzerlik varsa kelimeleri cok benzer kabul etmek icin kullanilacak fonksiyon.
Yer yer hatali benzerlik de tespit edebilir birbirinden cok alakasiz kelimeleri de alabilir ama genele vurunca 7 harf ustu ayni giden kelimeler birbirine asiri benzer anlamli oluyor.
Bu fonksiyonun sebebi mesela transformation ile transformations kelimesini ayni kabul etsin.
Bu kontrolu yapacak hazir fonksiyon bulamadigimdan kendim yazdim.
*/  int eslesme_sayisi = 0;
    while (*str1 != '\0' && *str2 != '\0'){
        if (*str1 == *str2){
            eslesme_sayisi++;
            if (eslesme_sayisi >= 6)
            {
                return 1; // True
            }
            str1++;
        }
        str2++;
    }
     return 0; // False
}



HOT_VECTOR *create_hot_vectors(int cumle_sayisi, int kelime_sayisi, SENTENCES sentences,DICTIONARY dictionary,int label1){//Hot vector olusturma fonksiyonu.
    HOT_VECTOR *hot_vectors = (HOT_VECTOR *)calloc(cumle_sayisi,sizeof(HOT_VECTOR));
    if (hot_vectors == NULL) {
        fprintf(stderr, "Bellek tahsisi hatasi\n");
        return NULL;
    }
    int i,j;
    for(i = 0;i<cumle_sayisi;i++){
        hot_vectors[i].hot_vector = (int*)calloc(kelime_sayisi,sizeof(int));
        if (hot_vectors[i].hot_vector == NULL) {
            fprintf(stderr, "Bellek tahsisi hatasi\n");
            return NULL;
        }
    }
    for(i = 0;i<cumle_sayisi;i++){
        char *token = strtok(sentences.cumleler[i]," ");
        hot_vectors[i].label = label1;
        while(token!=NULL){
            for(j = 0;j<kelime_sayisi;j++){
                if(strcmp(token, dictionary.sozluk[j]) == 0){
                    hot_vectors[i].hot_vector[j] = 1;
                    
                }
                else if(benzer_mi(token,dictionary.sozluk[j])){
                    hot_vectors[i].hot_vector[j] = 1;
                }
            }
            token = strtok(NULL," ");
        }
    }
    
    return hot_vectors;
}

void free_hot_vectors(HOT_VECTOR *hot_vectors, int cumle_sayisi) {//hot vector icin ayrilan alani serbest birakma fonksiyonu
	int i;
    for (i = 0; i < cumle_sayisi; i++) {
        free(hot_vectors[i].hot_vector);
    }
    free(hot_vectors);
}

void split_hot_vectors(HOT_VECTOR *hot_vectors, int total_size, int train_size, HOT_VECTOR **train_set, HOT_VECTOR **test_set) {//hot vektoru train ve test kumesine ayiriyoruz
    
    *train_set = (HOT_VECTOR *)malloc(train_size * sizeof(HOT_VECTOR));

    *test_set = (HOT_VECTOR *)malloc((total_size - train_size) * sizeof(HOT_VECTOR));

    if (*train_set == NULL || *test_set == NULL) {
        fprintf(stderr, "Bellek tahsisi hatasi\n");
        exit(EXIT_FAILURE);
    }

    int *indices = (int *)malloc(total_size * sizeof(int));
    int i;
    for (i = 0; i < total_size; ++i) {
        indices[i] = i;
    }
    //random dagitmak amacli.
    for (i = total_size - 1; i > 0; --i) {
        int j = rand() % (i + 1);
        int temp = indices[i];
        indices[i] = indices[j];
        indices[j] = temp;
    }
    // Eğitim kümesini doldur
    for (i = 0; i < train_size; ++i) {
        memcpy(&(*train_set)[i], &hot_vectors[indices[i]], sizeof(HOT_VECTOR));
    }
    // Test kümesini doldur
    for (i = train_size; i < total_size; ++i) {
        memcpy(&(*test_set)[i - train_size], &hot_vectors[indices[i]], sizeof(HOT_VECTOR));
    }

    free(indices);
}

void shuffle_hot_vectors(HOT_VECTOR *hot_vectors, int size) { //hot vektorleri random karistiriyoruz.
    int i;
    for (i = size - 1; i > 0; i--) {
        int j = rand() % (i + 1);

        // hot_vectors[i] ile hot_vectors[j] yer değiştir
        HOT_VECTOR temp = hot_vectors[i];
        hot_vectors[i] = hot_vectors[j];
        hot_vectors[j] = temp;
    }
}

HOT_VECTOR *merge_hot_vectors(HOT_VECTOR *hot_vectors1, int cumle_sayisi1, HOT_VECTOR *hot_vectors2, int cumle_sayisi2) {//2 hot vektor kumesini birlestiriyoruz.
    HOT_VECTOR *merged_hot_vectors = (HOT_VECTOR *)malloc((cumle_sayisi1 + cumle_sayisi2) * sizeof(HOT_VECTOR));
    int i;
    if (merged_hot_vectors == NULL) {
        fprintf(stderr, "Bellek tahsisi hatasi\n");
        return NULL;
    }

    // hot_vectors1'i kopyala
    for (i = 0; i < cumle_sayisi1; i++) {
        memcpy(&merged_hot_vectors[i], &hot_vectors1[i], sizeof(HOT_VECTOR));
    }

    // hot_vectors2'yi kopyala
    for (i = 0; i < cumle_sayisi2; i++) {
        memcpy(&merged_hot_vectors[cumle_sayisi1 + i], &hot_vectors2[i], sizeof(HOT_VECTOR));
    }
    shuffle_hot_vectors(merged_hot_vectors, cumle_sayisi1 + cumle_sayisi2); //birlestirirken karistiriyoruz

    return merged_hot_vectors;
}


double vektor_carpim(double *w,int *hot_vector,int boyut){ //vektor carpimi yapiyoruz
    double carpim =0 ;
    int i;
    for(i = 0;i<boyut;i++){
        carpim += w[i] *hot_vector[i];
    }
    return carpim;
}

double calculate_loss(double *w, HOT_VECTOR hot_vector,int boyut){ //tek bir loss hesaplamak icin
    double actual = hot_vector.label;
    double carpim =0 ;
    int i;
    for(i = 0;i<boyut;i++){
        carpim += w[i] * hot_vector.hot_vector[i];
    }
    double predicted = tanh(carpim);
    return pow((actual-predicted),2);
}

double calculate_mean_squared_error(double *w, HOT_VECTOR *Hot_Vectors,int boyut, int vektor_boyut){//toplam lossun ortalamasi
    double total_loss = 0;
    int i;
    for(i = 0;i<vektor_boyut;i++){
        total_loss += calculate_loss(w,Hot_Vectors[i],boyut);
    }
    return total_loss/vektor_boyut;
}

double *initialize_parameters(int vocab_size) {//random parametre baslatmak icin
    int i;
    double *parameters = (double *)malloc(vocab_size * sizeof(double));
    for (i = 0; i < vocab_size; i++) {
        parameters[i] = ((double)rand() / RAND_MAX) * 2 - 1; //-1 ile 1 arasi deger icin.
    }
    return parameters;
}

double calculate_accuracy(double *parameters, HOT_VECTOR *test_set, int vocab_size, int test_size) {//cumleleri bilme oranini test etme fonksiyonu.
    int correct_predictions = 0;
	int i;
    for (i = 0; i < test_size; i++) {
        double prediction = tanh(vektor_carpim(parameters, test_set[i].hot_vector, vocab_size));
        int predicted_label;
        if(prediction>= 0.9){
            predicted_label = 1;
        }
        if(prediction<=-0.9){
            predicted_label = -1;
        }

        if (predicted_label == test_set[i].label) {
            correct_predictions++;
        }
    }

    return (double)correct_predictions / test_size;
}

void gradient_descent(double *parameters, HOT_VECTOR *train_set, HOT_VECTOR *test_set, int vocab_size, int train_size, int test_size, int num_iterations, double learning_rate,char dosya_adi[],char w_dosya_isim[]) {
    int i,j,iteration = 0;
    printf("\n");
    FILE *dosya;
    FILE *w_Vector;
    w_Vector = fopen(w_dosya_isim, "w"); //her adimdaki w degerlerini tutuyoruz.
    dosya = fopen(dosya_adi, "w"); //dosyaya her adimda sure epoch accuracy loss gibi seyleri yazdiriyoruz.
    clock_t baslangic, bitis; //sure hesaplamak icin
    double sure = 0,accuracy,accuracy2,total_loss;
    total_loss = calculate_mean_squared_error(parameters, train_set, vocab_size, train_size);
    accuracy = calculate_accuracy(parameters, train_set, vocab_size, train_size);
    accuracy2 = calculate_accuracy(parameters, test_set, vocab_size, test_size);
    fprintf(dosya, "Gradient Time: %f Gradient Epoch: %d Loss: %f Train Accuracy: %f Test Accuracy: %f\n", sure, iteration, total_loss, accuracy,accuracy2);
    printf("GD Epoch %d Loss: %f Train Accuracy: %f Test Accuracy: %f\n", iteration, total_loss, accuracy,accuracy2);
    double *gradient = (double*)calloc(vocab_size,sizeof(double));
    do{
        
        for(i = 0; i<vocab_size;i++){
            fprintf(w_Vector,"%f ",parameters[i]);
        }
            fprintf(w_Vector,"\n");
        
        baslangic = clock();
        for(i = 0;i<vocab_size;i++){
            gradient[i] = 0;//bu lazim .
            for (j = 0; j < train_size; j++) {
                gradient[i] += 2*(tanh(parameters[i]*train_set[j].hot_vector[i]) - train_set[j].label) * train_set[j].hot_vector[i]* (1- pow(tanh(parameters[i]*train_set[j].hot_vector[i]),2));
            
            }
            
            parameters[i] -= learning_rate * gradient[i];
            
        }
        if (total_loss <= 0.05){ //belirli bir loss'tan sonra learning rate'i kademeli olarak azaltiyoruz.
            if(total_loss> 0.025){
                learning_rate -= 0.0005;
            }
        }
        
        bitis = clock();
        sure += ((double)(bitis - baslangic)) / CLOCKS_PER_SEC;
        iteration++;
        total_loss = calculate_mean_squared_error(parameters, train_set, vocab_size, train_size);
        accuracy = calculate_accuracy(parameters, train_set, vocab_size, train_size);
        accuracy2 = calculate_accuracy(parameters, test_set, vocab_size, test_size);
        fprintf(dosya, "Gradient Time: %f Gradient Epoch: %d Loss: %f Train Accuracy: %f Test Accuracy: %f\n", sure, iteration, total_loss, accuracy,accuracy2);
        printf("GD Epoch %d, Loss: %f, Train Accuracy: %f, Test Accuracy: %f\n", iteration, total_loss, accuracy,accuracy2);
        
    }while(iteration < num_iterations && total_loss >= 0.025);
    fclose(dosya);
    fclose(w_Vector);
    free(gradient);
}
void stochastic_gradient_descent(double *parameters, HOT_VECTOR *train_set,HOT_VECTOR *test_set, int vocab_size, int train_size,int test_size,int num_iterations, double learning_rate,char dosya_adi[],char w_dosya_isim[]) {
    
    int i,j,epoch = 0,k = 0;
    double total_loss,sure = 0,accuracy,accuracy2;
    FILE *dosya;
    FILE *w_Vector;
    w_Vector = fopen(w_dosya_isim, "w");
    dosya = fopen(dosya_adi, "w");
    double *mean_last_k_parameters = (double*)calloc(vocab_size,sizeof(double));
    clock_t baslangic, bitis;
    total_loss = calculate_mean_squared_error(parameters, train_set, vocab_size, train_size);
    accuracy = calculate_accuracy(parameters, train_set, vocab_size, train_size);
    accuracy2 = calculate_accuracy(parameters, test_set, vocab_size, test_size);
    fprintf(dosya, "SGD Time: %f SGD Epoch: %d Loss: %f Train Accuracy: %f Test Accuracy: %f\n", sure,epoch, total_loss, accuracy,accuracy2);
    printf("SGD Epoch %d, Loss: %f, Train Accuracy: %f Test Accuracy: %f\n", epoch, total_loss, accuracy,accuracy2);
    double *gradient1 = (double*)calloc(vocab_size,sizeof(double));
    do{
        for(i = 0; i<vocab_size;i++){
            fprintf(w_Vector,"%f ",parameters[i]);
        }
        fprintf(w_Vector,"\n");
        baslangic = clock();
        int random_train_batch[5];
        for(i = 0;i<5;i++){ //mini batch yapiyoruz
            random_train_batch[i] = rand() % train_size;
        }   
        for(i = 0;i<vocab_size;i++){
            gradient1[i] = 0; // bu lazim += yaptigimzdan ustte de lzmdi.
            for (j = 0; j < 5; j++) {
                gradient1[i] += 2*(tanh(parameters[i]*train_set[random_train_batch[j]].hot_vector[i]) - train_set[random_train_batch[j]].label) * train_set[random_train_batch[j]].hot_vector[i]* (1- pow(tanh(parameters[i]*train_set[random_train_batch[j]].hot_vector[i]),2));
            }
            gradient1[i] /= 5;
            parameters[i] -= learning_rate * gradient1[i];
            
        }
        bitis = clock();
        sure += ((double)(bitis - baslangic)) / CLOCKS_PER_SEC;
        epoch++;
        total_loss = calculate_mean_squared_error(parameters, train_set, vocab_size, train_size);
        accuracy = calculate_accuracy(parameters, train_set, vocab_size, train_size);
        accuracy2 = calculate_accuracy(parameters, test_set, vocab_size, test_size);
        fprintf(dosya, "SGD Time: %f SGD Epoch: %d Loss: %f Train Accuracy: %f Test Accuracy: %f\n", sure,epoch, total_loss, accuracy,accuracy2);
        printf("SGD Epoch %d, Loss: %f, Train Accuracy: %f Test Accuracy: %f\n", epoch, total_loss, accuracy,accuracy2);
        if (total_loss <= 0.05){
            if(total_loss> 0.025){
                learning_rate -= 0.001;
            }
        }
       
    }while(epoch < num_iterations && total_loss >= 0.025);
    free(gradient1);
    fclose(dosya);
    fclose(w_Vector);
}

void ADAM_Algorithm(double *parameters, HOT_VECTOR *train_set, HOT_VECTOR *test_set, int vocab_size, int train_size, int test_size, int num_iterations,double beta_1,double beta_2,double alpha,double epsilon,char dosya_adi[],char w_dosya_isim[]) {
    int i,j, epoch = 0;
    double total_loss,sure = 0,accuracy,accuracy2;

    FILE *dosya;
    FILE *w_Vector;
    w_Vector = fopen(w_dosya_isim, "w");
    dosya = fopen(dosya_adi, "w");
    clock_t baslangic, bitis;
     
    total_loss = calculate_mean_squared_error(parameters, train_set, vocab_size, train_size);
    accuracy = calculate_accuracy(parameters, train_set, vocab_size, train_size);
    accuracy2 = calculate_accuracy(parameters, test_set, vocab_size, test_size);
    fprintf(dosya, "ADAM Time: %f ADAM Epoch: %d Loss: %f Train Accuracy: %f Test Accuracy: %f\n", sure, epoch, total_loss, accuracy,accuracy2);
    printf("ADAM Epoch %d Loss: %f Train Accuracy: %f Test Accuracy: %f\n", epoch, total_loss, accuracy,accuracy2);
    double *m = (double*)calloc(vocab_size,sizeof(double));
    double *v = (double*)calloc(vocab_size,sizeof(double));
    double *gradient2 = (double*)calloc(vocab_size,sizeof(double));
    do{
        epoch++; //basta arttiriyoruz yoksa 0'a bolme durumu cikiyor. (B^0 = 0)
        for(i = 0; i<vocab_size;i++){
            fprintf(w_Vector,"%f ",parameters[i]);
        }
            fprintf(w_Vector,"\n");
        baslangic = clock();
        int random_train_batch[5];
        for(i = 0;i<5;i++){ //mini batch buna da yapsak iyi olur.
            random_train_batch[i] = rand() % train_size;
        }   
        for(i = 0;i<vocab_size;i++){
            
            for (j = 0; j < 5; j++) {
                gradient2[i] += 2*(tanh(parameters[i]*train_set[random_train_batch[j]].hot_vector[i]) - train_set[random_train_batch[j]].label) * train_set[random_train_batch[j]].hot_vector[i]* (1- pow(tanh(parameters[i]*train_set[random_train_batch[j]].hot_vector[i]),2));
            }
            gradient2[i] /= 5;
            m[i] = beta_1*m[i] + (1-beta_1)*gradient2[i];
            v[i] = beta_2*v[i] + (1-beta_2)*pow(gradient2[i],2);
            double mt_hat = m[i]/(1 - pow(beta_1,epoch));
            double vt_hat = v[i]/(1 - pow(beta_2,epoch));
            parameters[i] -=  (alpha*mt_hat)/(sqrt(vt_hat)+epsilon);
        }
        bitis = clock();
        sure += ((double)(bitis - baslangic)) / CLOCKS_PER_SEC;
        total_loss = calculate_mean_squared_error(parameters, train_set, vocab_size, train_size);
        accuracy = calculate_accuracy(parameters, train_set, vocab_size, train_size);
        accuracy2 = calculate_accuracy(parameters, test_set, vocab_size, test_size);
        fprintf(dosya, "ADAM Time: %f ADAM Epoch: %d Loss: %f Train Accuracy: %f Test Accuracy: %f\n", sure, epoch, total_loss, accuracy,accuracy2);
        printf("ADAM Epoch %d, Loss: %f, Train Accuracy: %f Test Accuracy: %f\n", epoch, total_loss, accuracy,accuracy2);
        
    }while(epoch < num_iterations && total_loss >= 0.025);
    fclose(dosya);
    free(m);
    free(v);
    free(gradient2);
    fclose(w_Vector);

}



double* copyVector(const double *source, int size) { //vektor kopyalamak icin
    double *destination = malloc(size * sizeof(double));
    if (destination == NULL) {
        // Bellek tahsisi başarısız oldu
        // Hata işleme kodları buraya eklenmeli
        exit(EXIT_FAILURE);
    }

    // Bellek alanını kopyala
    memcpy(destination, source, size * sizeof(double));

    return destination;
}



int main(){
    int i,j;
    remove_punctations("Tech.txt","Tech_no_punctuation.txt");
    remove_punctations("Economics.txt","Economics_no_punctuation.txt");
    merge_file("Tech_no_punctuation.txt","Economics_no_punctuation.txt","Tech_and_Economics_no_punctuation.txt");
    FILE *dosya1 = fopen("Tech_and_Economics_no_punctuation.txt", "r");
    if (dosya1 == NULL) {
        fprintf(stderr, "Dosya açma hatasi\n");
        return 1;
    }
    DICTIONARY dictionary;
    SENTENCES tech_sentences;
    SENTENCES economics_sentences;
    dictionary.kelime_sayisi = 0;
    dictionary.sozluk = NULL;
    tech_sentences.cumle_sayisi = 0;
    tech_sentences.cumleler = NULL;
    economics_sentences.cumle_sayisi = 0;
    economics_sentences.cumleler = NULL; 
    char cumle[MAX_CUMLE_UZUNLUGU];
    while (fgets(cumle, MAX_CUMLE_UZUNLUGU, dosya1) != NULL) { //fgets satir satir dosyayi okur.
        remove_newline(cumle);
        tokenize_and_store_unique_words(cumle, &dictionary.sozluk, &dictionary.kelime_sayisi);
    }
    fclose(dosya1);
    qsort(dictionary.sozluk, dictionary.kelime_sayisi, sizeof(const char*), compare_strings); //sozlukteki tum kelimeleri alfabetik siraliyoruz.
    
    /*printf("Farkli kelimeler:\n");
    for (i = 0; i < dictionary.kelime_sayisi; ++i) {
        printf("%s\n", dictionary.sozluk[i]);
    }
    printf("%d",dictionary.kelime_sayisi);*/

    seperate_sentences("Tech_no_punctuation.txt",&tech_sentences);

    /*printf("Teknoloji cumleleri:\n");
    for(i = 0;i<tech_sentences.cumle_sayisi;i++){
        printf("%s\n",tech_sentences.cumleler[i]);
    }
    printf("%d",tech_sentences.cumle_sayisi);*/
    
    seperate_sentences("Economics_no_punctuation.txt",&economics_sentences);

    /*printf("Ekonomi cumleleri:\n");
    for(i = 0;i<economics_sentences.cumle_sayisi;i++){
        printf("%s\n",economics_sentences.cumleler[i]);
    }
    printf("%d",economics_sentences.cumle_sayisi);*/

    int train_size_tech = (int)(tech_sentences.cumle_sayisi * 0.8); //%80 eğitim kümesi
    int test_size_tech = (int)(tech_sentences.cumle_sayisi - train_size_tech);
    int train_size_economics = (int)(economics_sentences.cumle_sayisi * 0.8);
    int test_size_economics = (int)(economics_sentences.cumle_sayisi - train_size_economics);
    int total_train_size = train_size_tech + train_size_economics;
    int total_test_size = test_size_economics +test_size_tech;

    HOT_VECTOR *hot_vectors_tech = create_hot_vectors(tech_sentences.cumle_sayisi,dictionary.kelime_sayisi,tech_sentences,dictionary,1); //Cikis degeri 1
    /*printf("Teknoloji dizisi hot vektorleri kontrol\n");
    for(j = 0;j<dictionary.kelime_sayisi;j++){
        printf("%s --- %d\n",dictionary.sozluk[j],hot_vectors_tech[1].hot_vector[j]);     
    }
    printf("Label = %d\n",hot_vectors_tech[1].label);*/

    HOT_VECTOR *hot_vectors_economics = create_hot_vectors(economics_sentences.cumle_sayisi,dictionary.kelime_sayisi,economics_sentences,dictionary,-1); //Cikis degeri -1

    /*printf("Ekonomi dizisi hot vektorleri kontrol\n");
    for(j = 0;j<dictionary.kelime_sayisi;j++){
        printf("%s --- %d\n",dictionary.sozluk[j],hot_vectors_economics[0].hot_vector[j]);     
    }
    printf("Label = %d\n",hot_vectors_economics[0].label);*/

    HOT_VECTOR *train_set_tech, *test_set_tech;
    split_hot_vectors(hot_vectors_tech, tech_sentences.cumle_sayisi, train_size_tech, &train_set_tech, &test_set_tech);
    
    
    HOT_VECTOR *train_set_economics, *test_set_economics;
    split_hot_vectors(hot_vectors_economics, economics_sentences.cumle_sayisi, train_size_economics, &train_set_economics, &test_set_economics);

    

    HOT_VECTOR *total_train_hot_vectors = merge_hot_vectors(train_set_tech,train_size_tech,train_set_economics,train_size_economics);
    HOT_VECTOR *total_test_hot_vectors = merge_hot_vectors(test_set_tech,test_size_tech,test_set_economics,test_size_economics);

    /*printf("Total test vektorler...\n");
    printf("total test size = %d",total_test_size);
    for(i = 0;i<total_test_size;i++){
        for(j = 0;j<dictionary.kelime_sayisi;j++){
            printf("%s ------ %d \n",dictionary.sozluk[j],total_test_hot_vectors[i].hot_vector[j]);
        }
        printf("Label = %d\n",total_test_hot_vectors[i].label);
    }*/
    //printf("\n%d",total_train_size);
    //printf("\n%d",total_test_size);
    //printf("\n%d",dictionary.kelime_sayisi);
    

    // double cikis = tanh(vektor_carpim(w1,total_test_hot_vectors[9].hot_vector,dictionary.kelime_sayisi));
    // printf("\n%lf",cikis);
    // double loss = calculate_loss(w1,total_test_hot_vectors[9],dictionary.kelime_sayisi);
    // printf("\n%d",total_test_hot_vectors[9].label);
    // printf("\n%lf",loss);
    // double total_loss = calculate_mean_squared_error(w1,total_test_hot_vectors,dictionary.kelime_sayisi,total_test_size);
    // printf("\n%lf",total_loss);
    srand(777);

    //w1 degerleri icin.
    double *parameters1_1 = initialize_parameters(dictionary.kelime_sayisi);
    double *parameters1_2 = copyVector(parameters1_1, dictionary.kelime_sayisi);
    double *parameters1_3 = copyVector(parameters1_1,dictionary.kelime_sayisi);
    gradient_descent(parameters1_1, total_train_hot_vectors,total_test_hot_vectors, dictionary.kelime_sayisi, total_train_size,total_test_size, 5000, 0.015,"w1_Gradient_values.txt","w1_GD_parameters.txt");
   
    stochastic_gradient_descent(parameters1_2,total_train_hot_vectors,total_test_hot_vectors,dictionary.kelime_sayisi,total_train_size,total_test_size,5000,0.09,"w1_SGD_values.txt","w1_SGD_parameters.txt");
  
    ADAM_Algorithm(parameters1_3,total_train_hot_vectors,total_test_hot_vectors,dictionary.kelime_sayisi,total_train_size,total_test_size,5000,0.8,0.888,0.1,0.00000001,"w1_ADAM_values.txt","w1_ADAM_parameters.txt");
    
    //w2 degerleri icin
    double *parameters2_1 = initialize_parameters(dictionary.kelime_sayisi);
    double *parameters2_2 = copyVector(parameters2_1, dictionary.kelime_sayisi);
    double *parameters2_3 = copyVector(parameters2_1,dictionary.kelime_sayisi);
    gradient_descent(parameters2_1, total_train_hot_vectors,total_test_hot_vectors, dictionary.kelime_sayisi, total_train_size,total_test_size, 5000, 0.015,"w2_Gradient_values.txt","w2_GD_parameters.txt");
    
    stochastic_gradient_descent(parameters2_2,total_train_hot_vectors,total_test_hot_vectors,dictionary.kelime_sayisi,total_train_size,total_test_size,5000,0.09,"w2_SGD_values.txt","w2_SGD_parameters.txt");

    ADAM_Algorithm(parameters2_3,total_train_hot_vectors,total_test_hot_vectors,dictionary.kelime_sayisi,total_train_size,total_test_size,5000,0.8,0.888,0.1,0.00000001,"w2_ADAM_values.txt","w2_ADAM_parameters.txt");

    //w3 degerleri icin
    double *parameters3_1 = initialize_parameters(dictionary.kelime_sayisi);
    double *parameters3_2 = copyVector(parameters3_1, dictionary.kelime_sayisi);
    double *parameters3_3 = copyVector(parameters3_1,dictionary.kelime_sayisi);
    gradient_descent(parameters3_1, total_train_hot_vectors,total_test_hot_vectors, dictionary.kelime_sayisi, total_train_size,total_test_size, 5000, 0.015,"w3_Gradient_values.txt","w3_GD_parameters.txt");
    
    stochastic_gradient_descent(parameters3_2,total_train_hot_vectors,total_test_hot_vectors,dictionary.kelime_sayisi,total_train_size,total_test_size,5000,0.09,"w3_SGD_values.txt","w3_SGD_parameters.txt");

    ADAM_Algorithm(parameters3_3,total_train_hot_vectors,total_test_hot_vectors,dictionary.kelime_sayisi,total_train_size,total_test_size,5000,0.8,0.888,0.1,0.00000001,"w3_ADAM_values.txt","w3_ADAM_parameters.txt");

    //w4 degerleri icin
    double *parameters4_1 = initialize_parameters(dictionary.kelime_sayisi);
    double *parameters4_2 = copyVector(parameters4_1, dictionary.kelime_sayisi);
    double *parameters4_3 = copyVector(parameters4_1,dictionary.kelime_sayisi);
    gradient_descent(parameters4_1, total_train_hot_vectors,total_test_hot_vectors, dictionary.kelime_sayisi, total_train_size,total_test_size, 5000, 0.015,"w4_Gradient_values.txt","w4_GD_parameters.txt");
    
    stochastic_gradient_descent(parameters4_2,total_train_hot_vectors,total_test_hot_vectors,dictionary.kelime_sayisi,total_train_size,total_test_size,5000,0.09,"w4_SGD_values.txt","w4_SGD_parameters.txt");

    ADAM_Algorithm(parameters4_3,total_train_hot_vectors,total_test_hot_vectors,dictionary.kelime_sayisi,total_train_size,total_test_size,5000,0.8,0.888,0.1,0.00000001,"w4_ADAM_values.txt","w4_ADAM_parameters.txt");

    //w5 degerleri icin
    double *parameters5_1 = initialize_parameters(dictionary.kelime_sayisi);
    double *parameters5_2 = copyVector(parameters5_1, dictionary.kelime_sayisi);
    double *parameters5_3 = copyVector(parameters5_1,dictionary.kelime_sayisi);
    gradient_descent(parameters5_1, total_train_hot_vectors,total_test_hot_vectors, dictionary.kelime_sayisi, total_train_size,total_test_size, 5000, 0.015,"w5_Gradient_values.txt","w5_GD_parameters.txt");
    
    stochastic_gradient_descent(parameters5_2,total_train_hot_vectors,total_test_hot_vectors,dictionary.kelime_sayisi,total_train_size,total_test_size,5000,0.09,"w5_SGD_values.txt","w5_SGD_parameters.txt");

    ADAM_Algorithm(parameters5_3,total_train_hot_vectors,total_test_hot_vectors,dictionary.kelime_sayisi,total_train_size,total_test_size,5000,0.8,0.888,0.1,0.00000001,"w5_ADAM_values.txt","w5_ADAM_parameters.txt");

   

    free(parameters1_1);
    free(parameters1_2);
    free(parameters1_3);
    free(parameters2_1);
    free(parameters2_2);
    free(parameters2_3);
    free(parameters3_1);
    free(parameters3_2);
    free(parameters3_3);
    free(parameters4_1);
    free(parameters4_2);
    free(parameters4_3);
    free(parameters5_1);
    free(parameters5_2);
    free(parameters5_3);
    for (i = 0; i < tech_sentences.cumle_sayisi; i++) {
        free(tech_sentences.cumleler[i]);
    }
    free(tech_sentences.cumleler);

    for (i = 0; i < economics_sentences.cumle_sayisi; i++) {
        free(economics_sentences.cumleler[i]);
    }
    free(economics_sentences.cumleler);

    for (i = 0; i < dictionary.kelime_sayisi; ++i) {
        free(dictionary.sozluk[i]);
    }
    free(dictionary.sozluk);
    free_hot_vectors(hot_vectors_tech, tech_sentences.cumle_sayisi);
    free_hot_vectors(hot_vectors_economics, economics_sentences.cumle_sayisi);
    free_hot_vectors(train_set_tech, train_size_tech);
    free_hot_vectors(test_set_tech, test_size_tech);
    free_hot_vectors(train_set_economics, train_size_economics);
    free_hot_vectors(test_set_economics, test_size_economics);
    free_hot_vectors(total_test_hot_vectors,total_test_size);
    free_hot_vectors(total_train_hot_vectors,total_train_size);
    return 0;
}


void remove_punctations(const char* girdi_dosyasi, const char* cikti_dosyasi){
    FILE* giren = fopen(girdi_dosyasi, "r");
    if (giren == NULL) {
        perror("Giris dosyasini acarken hata olustu");
        return;
    }
    FILE* cikan = fopen(cikti_dosyasi, "w");
    if (cikan == NULL) {
        perror("Cikis dosyasini açarken hata oluştu");
        fclose(cikan);
        return;
    }
    char karakter;
    while((karakter = fgetc(giren)) != EOF){
        if(!ispunct(karakter)){
            fputc(karakter,cikan);
        }
    }
    fclose(giren);
    fclose(cikan);
    printf("Noktalama isaretleri kaldirilarak \"%s\" dosyasina yazildi.\n", cikti_dosyasi);
}

void remove_newline(char *str) {
    char *newline = strchr(str, '\n');
    if (newline != NULL) {
        *newline = '\0';
    }
}

void tokenize_and_store_unique_words(char *cumle, char ***kelimeler, int *kelime_sayisi) {
    char *kelime = strtok(cumle, " "); // BOSLUK karakterine gore ayristirma.
    int i;
    while (kelime != NULL) {
        int isUnique = 1;  //Kontrol noktasi.

        // Daha önce eklenmiş mi kontrol et
        for (i = 0; i < *kelime_sayisi; ++i) {
            if (strcasecmp((*kelimeler)[i], kelime) == 0) { //Ayni kelime var mi kontrol.
                isUnique = 0;
            }
        }

        // Eğer daha önce eklenmemişse, ekleyin
        if (isUnique) {
            (*kelimeler) = realloc((*kelimeler), (*kelime_sayisi + 1) * sizeof(char *)); //Yer ayirma.
            char *kucuk_harfli_kelime = strdup(kelime); //kelimelerimizi kucuk harfe cevirip sozlugumuze ekleyecegiz.

            // Tüm harfleri küçük harfe çevir
            for (i = 0; kucuk_harfli_kelime[i]; i++) {
                kucuk_harfli_kelime[i] = tolower(kucuk_harfli_kelime[i]);
            }

            (*kelimeler)[*kelime_sayisi] = kucuk_harfli_kelime;
            (*kelime_sayisi)++;
    
        }

        kelime = strtok(NULL, " ");
    }
}

void merge_file(const char *ilkdosya, const char *ikincidosya, const char *birlesik_dosya) {
    FILE *dosya1 = fopen(ilkdosya, "r");
    FILE *dosya2 = fopen(ikincidosya, "r");
    FILE *birlesikDosya = fopen(birlesik_dosya, "w");

    if (dosya1 == NULL || dosya2 == NULL || birlesikDosya == NULL) {
        printf("Dosya acma hatasi\n");
        return;
    }

    char karakter;

    // Ilk dosyadan okuma yapip birlesecek dosyaya yaziyoruz.
    while ((karakter = fgetc(dosya1)) != EOF) {
        fputc(karakter, birlesikDosya);
    }
    fputc('\n',birlesikDosya);
    // Ikinci dosyadan okuma yapip birlesecek dosyaya yaziyoruz.
    while ((karakter = fgetc(dosya2)) != EOF) {
        fputc(karakter, birlesikDosya);
    }

    fclose(dosya1);
    fclose(dosya2);
    fclose(birlesikDosya);

    printf("Dosyalar birlestirildi ve %s adli dosyaya yazildi.\n", birlesik_dosya);
}

int compare_strings(const void *a, const void *b) {
    return strcmp(*(const char**)a, *(const char**)b);
}

void seperate_sentences(const char *dosyaAdi, SENTENCES *sentences) {
    FILE *dosya = fopen(dosyaAdi, "r");
    int i;
    if (dosya == NULL) {
        perror("Dosya acma hatasi");
        exit(EXIT_FAILURE);
    }

    char cumle[MAX_CUMLE_UZUNLUGU];
    sentences->cumle_sayisi = 0;

    while (fgets(cumle, sizeof(cumle), dosya) != NULL) {
        sentences->cumleler = realloc(sentences->cumleler, (sentences->cumle_sayisi + 1) * sizeof(char *));
        if (sentences->cumleler == NULL) {
            perror("Bellek tahsis hatasi");
            exit(EXIT_FAILURE);
        }

        remove_newline(cumle);

        for(i = 0;i<strlen(cumle);i++){
            cumle[i] = tolower(cumle[i]);
        }
        sentences->cumleler[sentences->cumle_sayisi] = malloc(strlen(cumle) + 1);
        if (sentences->cumleler[sentences->cumle_sayisi] == NULL) {
            perror("Bellek tahsis hatasi");
            exit(EXIT_FAILURE);
        }
        strcpy(sentences->cumleler[sentences->cumle_sayisi], cumle);

        // Cümle sayısını artırma
        sentences->cumle_sayisi++;
    }

    printf("%s dosyasindaki cumleler alindi.", dosyaAdi);

    fclose(dosya);
}

