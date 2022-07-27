Flask Application. 

-Register Ad,soyad, cinsiyet, alıp mongodb de users collection una kaydetsin. Kullanıcının Purchased_Service kısmı bulunsun.
-purchase Ad ve soyad ve odeme_miktari(number) alsın. 
-Odeme 100 TL ise mongodb de bu isim ve soyaisme sahip kullanıcının purchased_services bölümü True olarak güncellensin.
-Paid_service İçine ad ve soyad alması yeterli.
- Eğer kullanıcı servisi daha önce satın aldıysa burdan alacağı cevap ‘Hoşgeldiniz servisler tekrar kullanıma açıktır.’ olsun ve servis tek kullanımlık olduğu için
Purchased_services bölümü False olarak güncellensin. Aynı kullanıcı tekrar istek atarsa aşağıdaki cevabı alsın. 
- Satın almadıysa ‘Bu servisi kullanmak için satın almalısınız ’ cevabı gelsin.



#Bu uygulamada yazılım olarak python flask ve veri tabanı olarak mongoDb kullandım. Yalnızca saf bir back end uygualaması çıkararak Postman dan gönderdiğim test verilerini
MongoDb ye kaydederek gerçek hayatta kullanılabilecek bir ödeme servis uygulamasını geliştirdim.
