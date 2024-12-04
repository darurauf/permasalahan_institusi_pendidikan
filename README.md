## Business Understanding

Institusi pendidikan ini bertujuan untuk memahami faktor-faktor yang memengaruhi status kelulusan mahasiswa (graduate atau dropout). Dengan analisis ini, institusi berharap dapat mengidentifikasi karakteristik yang berkontribusi terhadap keberhasilan akademis dan penyelesaian program studi. Hal ini diharapkan dapat membantu institusi dalam merancang strategi intervensi untuk meningkatkan tingkat kelulusan dan mengurangi angka dropout, serta mendukung mahasiswa dalam perjalanan akademis mereka.

### Permasalahan Bisnis

Institusi pendidikan ini menghadapi beberapa permasalahan penting yang memerlukan perhatian, khususnya terkait dengan tingkat dropout yang tinggi. Beberapa permasalahan utama adalah:

1. Tingkat Dropout yang Tinggi: Mahasiswa yang gagal menyelesaikan program studi tepat waktu atau yang meninggalkan studi mereka dapat berdampak negatif pada reputasi institusi dan menyebabkan pemborosan sumber daya. Jika angka dropout terus meningkat, institusi berisiko kehilangan kepercayaan dari calon mahasiswa dan pihak pemangku kepentingan lainnya.

2. Keseimbangan Kehidupan dan Studi yang Kurang Optimal: Banyak mahasiswa yang menghadapi tantangan dalam menyeimbangkan tuntutan akademik dengan kehidupan pribadi. Ketidakseimbangan ini bisa menyebabkan kelelahan, stres, dan pada akhirnya, keputusan untuk menghentikan studi.

3. Ketidakpuasan terhadap Program Studi: Mahasiswa yang merasa kurang relevan atau tidak puas dengan program studi yang diambil memiliki kemungkinan lebih tinggi untuk dropout. Jika permasalahan ini tidak diatasi, institusi mungkin akan kesulitan untuk menarik dan mempertahankan mahasiswa.

Urgensi dan Dampak Jangka Panjang: Tingkat dropout yang tinggi dapat berdampak negatif pada citra institusi dan mengurangi kepercayaan dari masyarakat. Selain itu, angka dropout yang tinggi juga menghambat upaya institusi dalam mencetak lulusan berkualitas. Oleh karena itu, penting untuk memahami faktor-faktor yang berkontribusi terhadap dropout dan merancang solusi untuk meningkatkan keberhasilan akademik mahasiswa.

### Cakupan Proyek

Proyek ini bertujuan untuk melakukan analisis mendalam terhadap data demografi, pekerjaan, dan kepuasan karyawan guna memahami faktor-faktor yang berkontribusi terhadap tingkat attrition karyawan. Berikut adalah rincian cakupan proyek:

Pekerjaan yang Akan Dilakukan:
1. Pengumpulan Data: Meliputi data demografi mahasiswa, serta data terkait tingkat kehadiran dan keterlibatan dalam perkuliahan.
2. Praproses Data: Melakukan pembersihan data untuk menghilangkan missing values, dan melakukan encoding untuk data kategorikal. Hal ini penting untuk memastikan data yang digunakan dalam analisis akurat dan relevan.
3. Analisis Hubungan Antarvariabel: Menerapkan teknik analisis, seperti analisis korelasi untuk mengeksplorasi hubungan antara variabel-variabel yang berbeda terhadap tingkat attrition.
4. Modeling dan Prediksi: Mengembangkan model prediksi untuk mengidentifikasi faktor-faktor risiko yang berkontribusi terhadap attrition menggunakan teknik machine learning. Model ini diharapkan dapat memberikan wawasan mengenai potensi karyawan yang berisiko tinggi untuk keluar.
5. Visualisasi Data: Membuat dashboard visualisasi yang interaktif untuk mempresentasikan temuan analisis, memudahkan manajemen dalam memahami data, serta memfasilitasi pengambilan keputusan yang berbasis data.

Batasan Proyek:
1. Proyek ini akan fokus pada data mahasiswa yang tersedia dalam periode tertentu dan tidak mencakup data dari luar sumber yang ditentukan.
2. Analisis akan terbatas pada faktor-faktor yang dapat diukur secara kuantitatif dan kualitatif dari survei yang telah dilakukan.
3. Proyek tidak akan mencakup implementasi dari rekomendasi kebijakan yang dihasilkan.

Target Proyek:
1. Meningkatkan pemahaman terhadap faktor-faktor yang memengaruhi kelulusan atau dropout mahasiswa.
2. Menghasilkan rekomendasi berbasis data untuk menurunkan tingkat dropout dan meningkatkan efektivitas program studi.

Output Akhir dari Proyek:
1. Model Prediksi: Model yang dapat memprediksi kemungkinan mahasiswa akan graduate atau dropout.
2. Dashboard Visualisasi Data: Sebuah dashboard interaktif yang menyajikan hasil analisis dan memungkinkan manajemen untuk mengeksplorasi data dengan lebih mendalam.

### Persiapan

Sumber Data yang digunakan adalah employee_data.csv, yang mencakup beberapa kolom penting seperti:

1. Marital_status: Status perkawinan mahasiswa.
2. Admission_grade: Nilai masuk mahasiswa.
3. Age_at_enrollment: Usia mahasiswa pada saat pendaftaran.
4. Status: Status akhir mahasiswa (graduate atau dropout).
5. Curricular_units_1st_sem_grade: Nilai akademik pada semester pertama.
6. Curricular_units_2nd_sem_grade: Nilai akademik pada semester kedua.

Link streamlit cloud: https://tesdata-mznd73jiuyqg62pnojc63l.streamlit.app/

Setup environment:

```
cd C:\Users\<user>\Downloads
java -jar metabase.jar
http://localhost:3000
```

## Business Dashboard

Dashboard bisnis dapat dibuat untuk memvisualisasikan data-data kunci seperti:

1. Grafik Jumlah Dropout:
Grafik ini menampilkan total jumlah mahasiswa yang dropout selama periode tertentu. Dengan melihat jumlah ini secara keseluruhan, institusi dapat memahami tren dropout dan mengevaluasi dampak dari berbagai kebijakan atau perubahan program studi yang dilakukan.

2. Grafik Dropout Berdasarkan Rata-Rata Nilai Semester 1:
Grafik ini mengelompokkan mahasiswa dropout berdasarkan nilai akademik mereka di semester pertama. Dengan melihat pola dropout terhadap rata-rata nilai, institusi dapat mengidentifikasi jika performa di semester pertama memengaruhi kecenderungan untuk dropout. Mahasiswa dengan nilai rendah di semester ini mungkin memerlukan dukungan tambahan untuk mencegah dropout.

3. Grafik Dropout Berdasarkan Rata-Rata Nilai Semester 2:
Grafik ini menunjukkan hubungan antara rata-rata nilai semester kedua dan status dropout. Grafik ini dapat membantu menentukan apakah performa pada semester kedua berdampak pada keputusan mahasiswa untuk melanjutkan atau menghentikan studinya. Nilai rendah pada semester ini dapat mengindikasikan tantangan akademik yang memerlukan perhatian lebih.

4. Grafik Dropout Berdasarkan Persentase Pengangguran:
Grafik ini menampilkan hubungan antara tingkat dropout dan persentase pengangguran di wilayah atau periode tertentu. Tingkat pengangguran yang tinggi mungkin mencerminkan kondisi ekonomi yang sulit, yang bisa memengaruhi keputusan mahasiswa untuk melanjutkan atau keluar dari studi mereka. Institusi dapat mempertimbangkan untuk memberikan dukungan finansial atau karier di tengah kondisi ekonomi yang menantang.

## Menjalankan Sistem Machine Learning

```
pip install -r requirements.txt
streamlit run prediksi_model_streamlit.py
```

## Conclusion

Berdasarkan analisis data mahasiswa, beberapa faktor utama yang berkontribusi terhadap status kelulusan atau dropout telah diidentifikasi. Faktor-faktor ini termasuk performa akademis di semester pertama dan kedua, serta tingkat pengangguran yang memengaruhi stabilitas ekonomi dan motivasi mahasiswa. Data menunjukkan adanya hubungan signifikan antara kesiapan akademik awal dan kondisi ekonomi dengan kemungkinan mahasiswa untuk berhasil atau dropout.

Karakteristik umum dari mahasiswa yang berisiko tinggi untuk dropout meliputi:

Performa Akademis yang Rendah pada Semester Awal: Mahasiswa yang kesulitan secara akademis pada semester pertama dan kedua memiliki kecenderungan lebih tinggi untuk dropout. Intervensi akademis pada tahap awal dapat membantu mahasiswa ini tetap berada di jalur studi.

Pengaruh Ekonomi: Tingkat pengangguran yang tinggi dapat menambah tekanan bagi mahasiswa untuk mencari pekerjaan lebih awal, yang bisa menghambat keberlanjutan studi mereka. Dalam kondisi ekonomi yang sulit, institusi dapat mempertimbangkan program dukungan untuk membantu mahasiswa mempertahankan fokus akademis mereka.

Dengan memahami faktor-faktor ini, institusi pendidikan dapat merancang intervensi yang lebih tepat sasaran untuk menurunkan tingkat dropout dan mendukung keberhasilan akademik mahasiswa. Upaya ini diharapkan tidak hanya meningkatkan tingkat kelulusan, tetapi juga membantu mahasiswa mencapai potensi akademik mereka, yang pada gilirannya akan berdampak positif pada reputasi dan kualitas institusi.

## Rekomendasi Action Items
Berdasarkan temuan dari analisis data, berikut adalah beberapa langkah rekomendasi yang dapat diambil oleh institusi untuk mengurangi tingkat dropout dan meningkatkan tingkat kelulusan:

1. Dukungan Akademik pada Semester Awal
Deskripsi: Mahasiswa dengan performa rendah pada semester pertama dan kedua cenderung memiliki risiko dropout lebih tinggi. Institusi dapat menyediakan program bimbingan atau pendampingan akademik khusus bagi mahasiswa yang kesulitan di awal studi.
Action Item: Menyediakan program mentor atau tutor bagi mahasiswa pada semester pertama, terutama bagi mereka yang mendapatkan nilai rendah.
Implementasi: Program dapat dimulai dengan mengidentifikasi mahasiswa yang berisiko berdasarkan nilai semester pertama, lalu memberikan pilihan sesi bimbingan mingguan, baik secara individual maupun dalam kelompok kecil.

2. Peningkatan Keseimbangan Kehidupan dan Studi
Deskripsi: Ketidakseimbangan antara tuntutan akademik dan kehidupan pribadi dapat menyebabkan stres dan burnout pada mahasiswa, yang memengaruhi keputusan untuk dropout.
Action Item: Menawarkan workshop manajemen waktu dan stres kepada mahasiswa, terutama selama periode ujian atau tugas akhir semester.
Implementasi: Workshop dapat dilakukan secara berkala melalui sesi online maupun tatap muka, dihadiri oleh konselor atau pembicara yang berpengalaman dalam manajemen stres dan pengembangan diri.

3. Program Intervensi untuk Mahasiswa yang Berasal dari Wilayah dengan Tingkat Pengangguran Tinggi
Deskripsi: Kondisi ekonomi dapat memengaruhi motivasi mahasiswa untuk menyelesaikan studi mereka. Mahasiswa dari wilayah dengan tingkat pengangguran tinggi mungkin merasakan tekanan untuk segera bekerja atau kesulitan membiayai pendidikan.
Action Item: Menyediakan bantuan finansial atau beasiswa khusus bagi mahasiswa yang berasal dari daerah dengan tingkat pengangguran tinggi atau kondisi ekonomi menantang.
Implementasi: Institusi dapat melakukan survei untuk mengidentifikasi mahasiswa yang berasal dari latar belakang ini dan memberikan opsi bantuan finansial atau beasiswa berbasis kebutuhan.

Dengan menerapkan action items di atas, institusi pendidikan diharapkan dapat menurunkan tingkat dropout, mendukung keberhasilan akademik mahasiswa, dan membangun reputasi yang lebih baik sebagai institusi yang peduli terhadap kebutuhan dan perkembangan mahasiswanya. Strategi ini juga akan membantu mahasiswa dalam mencapai tujuan akademik dan karier mereka secara efektif, yang pada akhirnya berdampak positif pada perkembangan dan keberhasilan institusi.
