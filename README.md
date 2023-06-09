# A.	AĞ SİMÜLASYON PROGRAMLARI

Gelişen teknoloji ve günümüz ihtiyaçlarının giderek artış göstermektedir. Bu artışın, gelişimin sonucu olarak gereksinimlerin de fazlasıyla artması ve daha karmaşık hale gelmesi ile birlikte, deney maliyetleri artması gerçek hayatta geliştirilmek istenen herhangi bir projenin de toplam maliyeti açısından oldukça yük getirmiştir. Buna çözüm olarak simülasyonlar çok önemli bir görevi üstlenmiş olmaktadır.  Maliyet kazancının yanı sıra zaman, iş güvenliği açısından da oldukça fayda sağlamaktadır. Ağ simülasyon programları da zaman, mekân, maliyet gibi yükleri hafifletmektedir. Bunu yanında öngörülemeyen problemlerin tespiti ve çözümü aşamasında da oldukça fayda sağlamaktadır.
<br><br>

## 1.	GNS3 (Graphical Network Simulator 3):

Açık kaynak kodlu bir emülatör  olan bu program, özellikle Cisco IOS’ları emüle ederek sanki gerçek dünyadaki bir cihazda üzerinde çalışıyormuş gibi uygulamalar geçekleştirilebilmektedir. GNS3 Cisco IOS’ları emüle ederken( benzetim) Dynamips isimli programı kullanır. GNS3 programı da Dynamips için grafiksel bir arabirim sunar. 

<br>
 <img src="https://github.com/yilmazcelikk002/UygulamaProjesi/assets/132395836/1162487c-596d-40ee-97d1-06779c560088" align="center" width="480" height="320">
<br><br>

GNS3 bir başka önemli özelliği de farklı markaların işletim sistemlerini emüle edebilmesidir. Bunun yanında Wmvare gibi sanal makine programları ile oluşturacağınız sanal makineler üzerinden farklı topolojiler oluşturabilir, bu sanal makinelerin birbirleri ile haberleştirebilmesine olanak sağlamaktadır. GNS3 yazılımının kurulmasıyla Wireshark adındaki ağ izleme, paket yakalama yazılımları da beraberinde kurulmaktadır. Bundan dolayı ağ trafiğini izlemek mümkün hale gelmektedir.

Reel dünyadaki yönlendirici ile gerçek sanal bilgisayarlar kullanılmasından dolayı epey gerçekçi bir çalışma ortamı sağlamaktadır. Emülatörün bir diğer önemli özelliği de sanal ağda kullanılan sanal makinaların fiziksel bilgisayar üzerinden internete çıkabilmesidir.
<br><br>

## 2.	OMNeT++ (Objective Modular Network Testbed in C++):

OMNeT++, nesne yönelimli modüler yapılı bir ağ simülasyon programıdır. Belli bir alana ya da mimariye özel bir yapıda değil daha genel bir mimariye sahip denilebilir. Genelden kasıt çeşitli alanlar, farklı mimariler,  farklı sistemleri modellemek mümkündür.<br><br>
•	Kablolu veya kablosuz ağların simülasyonundan<br>
•	Protokol simülasyonundan<br>
•	Kuyruk ağ yapılarının simülasyonundan<br>
•	Çok işlemcili sistemlerinin simülasyonundan<br>
•	Dağıtık donanım sistemlerinin simülasyonundan<br>
•	Kompleks yazılım sistemlerinin performans yönlerinin değerlendirilmesi<br>
•	Ayrık olay yaklaşımının uygun olduğu ve mesaj alışverişi yoluyla iletişim kuran varlıklara uygun şekilde eşlenebildiği herhangi bir sistemin simülasyonu.<br>

Günümüzde sıklıkla kullanılmakta olan iletişim ağlarının modellenmesini sağlar. OMNeT++, aslında normal bir simülasyon programından farklı olarak direk simüle etmek üzerine değil de bunun yerine simülasyon oluşturmak için altyapı ve araç sunar. Bu yapının temel bileşenlerinden biri simülasyon modelleri için bir bileşen mimarisidir. Simülasyon, modül adı verilen kullanıcı tarafından oluşturulan ve tekrar tekrar kullanılabilir yapıların birleşimiyle oluşturulur. Modüller bir nevi usercontrol’a benzetmek mümkündür istenildiği yerde kullanılabilmektedir.

<img src="https://github.com/yilmazcelikk002/UygulamaProjesi/assets/132395836/77c6bd65-7cc7-48f7-9cd4-bf3589d62b6f" align="center" width="320" height="180">
 <br> 
 
Modüller, kapılar aracılığıyla birbirine bağlanır. Bu modüllerin birleşiminde bileşik modüller oluşturulur.  Modüller, mesajlar, kanallar ve kapılar gibi yeniden kullanılabilir bileşenlerden ağ modelleri oluşturmak için bir yapı sağlar. Modüller, mesajların isteğe bağlı veri yapıları taşıyabileceği mesaj geçişi yoluyla iletişim kurar. 
  
<img src="https://github.com/yilmazcelikk002/UygulamaProjesi/assets/132395836/c28e7ddb-6da1-472b-abb2-e014f970a82c" align="center" width="480" height="320">
  <br>
  
OMNeT++, C++ programlama dili ile yazılmıştır, simülasyonların oluşturulmasını, kullanımını basitleştirmek ve görselliği daha anlaşılır hale getirmek için bir grafik kullanıcı arabirimi (GUI) bulunmaktadır. NED adı verilen ağ tanımlama dili kullanır. Gelişmiş bir simülasyon kütüphanesine sahiptir. Simüle edilecek olan tüm nesneler statik ya da dinamik olarak oluşturulabilmektedir. Bu simülasyon yazılımı ücretsizdir ve zengin doküman desteğine sahiptir.

<br><br>

## 3.	OPNET Modeler (OPtimum NETwork performance):

OPNET Modeler, iletişim sistemleri ve haberleşme ağlarının simüle etmek için gerçekçi bir ortam sağlayan nesneye yönelik bir simülasyon yazılımıdır. OPNET Modeler üzerinden tasarlanan sistemler ayrık zamanlı simülasyon gerçekleştirilerek başarım analizleri yapılabilmektedir. OPNET genel olarak başarım ölçümü, trafik planlaması, ağ yönetimi, ağ tasarımı, ürünlerin ve protokollerin testi, protokol tasarımı, başarım değerlendirmesi Başarım optimizasyonu, ağ yönetimi gibi durumlarda rahatlıkla kullanılabilmektedir.
<br>
OPNET hiyerarşik modelleme katmanlarından oluşur. OPNET zengin kütüphane içeriğini bünyesinde barındırmaktadır. ATM, TCP/IP, MPLS gibi ağ protokollerinin, 3Com, Cisco, Bays Network gibi önde gelen firmaların ürünlerinin modellerini içerir. OPNET’in önemli avantajlarından birisi bünyesinde barındırdığı editörler aracılığı ile yeni protokol ve ürünlerin modellerini oluşturabilmesidir. Sonrasında bu modellerin model kütüphanesine eklenmesine olanak sağlamasıdır. 

#### OPNET Modeler Temel Özellikleri:

•	Özellikleri biçimlendirilebilen nesnelerden oluşur.<br>
•	Bilgi ve haberleşme sistemleri ile ilgili pek çok yapı sağlar örneğin dağıtılmış sistemler ve ağların modellenmesi gibi<br>
•	OPNET hiyerarşi modelleri temele alır.<br>
•	Modellerin oluşturulması grafiksel editörler aracılığı ile sağlanır.<br>
•	Modellerin C yazılım dilinde otomatik olarak derlenmesi mümkündür. <br>
•	OPNET simüle etme süresi boyunca otomatik olarak pek çok performans istatistiği sunar. Ayrıca yeni istatistikleri tanımlama imkanı da sunmaktadır.<br>
•	OPNET simülasyon sonuçlarını grafiksel olarak sunmak için gelişmiş birtakım araçlara sahiptir.<br>
•	Modellerin çalışmalarını bir animasyon şeklinde gözlemlemek mümkündür.<br>

<img src="https://github.com/yilmazcelikk002/UygulamaProjesi/assets/132395836/a75d7f7d-edb5-4062-82d7-15cac2ed9da3" align="center" width="480" height="320">
<br>

OPNET Modeler programında bir sistemi modellemek için, birbirinden farklı görevleri bulunan editörler kullanılmaktadır. Bu editörlerde yapılan işlemler sonrasında birleştirilerek modelleme tamamlanır. Bu editörler;
 
<br>•	Project Editör: Ağ modellerinin geliştirildiği, alt ağların oluşturulduğu, bağlantı hatları, düğümler(nodes) ve coğrafik içeriğin tanımlandığı editördür.
<br>•	Düğüm (Node) Model Editör: Proje editöründe kullanılan ağ modellerindeki nesnelerin(switch, router, Workstation vb.düğümlerin) geliştirildiği editördür.
<br>•	Proses (Process) Model Editör: Düğüm editöründeki nesnelerin yapısının, işlevinin, parametrelerinin ve davranışlarının tanımlandığı, kontrol edildiği ve değiştirildiği editördür.
<br>•	Bağlantı (Link) Model Editör: Ağ modellerinin/cihazlarının iletişimini sağlayan bağlantı (veri yolu, ara bağlantı vb.) modellerinin oluşturulduğu ve düzenlendiği editördür.
<br>•	Paket Biçim (PacketFormat) Editörü: Veri, kontrol gibi bilgi paketlerinin tanımlandığı ve yapılarının geliştirildiği editördür.
<br><br>

## 4.	NS-2(Network Simülatör) 
Network Simülatör-2 temelde C++ programlama dili ile yazılmış bir simülatördür. Ancak C++ dili ile yazılmış olan modüllerin yüksek seviyeli bir dil olan OTcl dili ile yazılmış kodlar aracılığıyla ile yapmaktadır. Ayrıca OTcl dilini modelleme yaparken kullanılacak senaryonun yazılması için kullanılmaktadır. Yani OTcl’e bir ekleme yapılmak istendiği zaman, eklemenin ait modülün C++ dili ile yazılması gerekmektedir.

Ns-2 LAN, WAN ve VPN gibi ağları simüle etmek için kullanılabilmektedir.

 
<img src="https://github.com/yilmazcelikk002/UygulamaProjesi/assets/132395836/a0f99860-aadc-42f3-9126-72c21e69469f" align="center" width="480" height="320">
<br>

Ns-2 ile oluşturulan bir simülasyonun analizinde elde edilecek veriler iki ayrı şekilde oluşturulmaktadır. Birincisi, tarihçe dosyası (trace files) olarak isimlendirilen ve uzantısı  tr bir dosya oluşturulmaktadır.. Bu dosya, bir nevi LOG kayıtlarını tutan bir doküman gibi düşünülebilir. İçerinde bu doküman, bir alıcı ne zaman bilgi alışverişinde bulunduğu, ne zaman bu bilgileri kayıt altına aldı gibi bilgiler yer almaktadır. İkinci olarak ise, Network Animator (NAM) adındaki dosyada ise yazılan modelini modüllerin kodlarına göre algılayıcıların paket bilgilerini, hareketlerini biri nevi görsel olarak sonuçları çıktıları sunan dosya denilebilir.

<br><br>

## 5.	NS-3(Network Simülatör) 

NS-3 ağ simülatörü, ayrık olay temeline dayanmaktadır. NS-3’ün yazılımı Python ile C++ ve Python programlama dilleri ile yazılmıştır. Açık kaynak kodlu bir proje olan NS-3 2006’da geliştirilmeye başlanmıştır. NS-3 simülatörü, ismine bakıldığı zamanNS-2’nin genişletilmiş hali gibi gözükse de değildir, yeni ve farklı bir ağ simülatörüdür. 

 <img src="https://github.com/yilmazcelikk002/UygulamaProjesi/assets/132395836/c98a4a0b-1fbc-43f1-a45b-e5c6987a1166" align="center" width="480" height="320">
<br><br>


NS-3 her ne kadar NS-2 den farklı olarak ortaya çıkmış olsa da temel mimariyi, modelleri, bileşenlerini ve entegrasyonunu NS-2 den esinlenerek geliştirmeye odaklanmıştır. NS-2’den farklı olarak NS-3, komutların bulunduğu dosyayı oluşturmak için OTcl’yi kullanmaz. NS-3 betikleri, komutları oluşturmak ve simülasyonları tanımlamak için Python ve C++ programlama dillerini kullanmaktadır.

NS-3 Windows, Linux ve Unix tabanlı işletim sistemleri üzerinde çalışabilen bir ağ simülatörüdür. NS-3 temelde IPv6 ve IPv4 tabanlı ağları oluşturmaya odaklanmıştır. <br><br>Bu yazılımın temel özelliklerine bakıldığında; <br>
•	Simülasyon için gerçekçi animasyon desteği. NS-3 ağ simülatöründe NetAnim (Network Animator) ara yüz sayesinde gerçekleştirilen simülasyonu çevrimdışı olarak izlenebilmektedir.<br>
•	Sanal ağların yapısı ve olay zamanlayıcı, topoloji üreteçleri, zamanlayıcılar, rastgele değişkenler gibi nesneler için destek ve internet tabanlı ve diğer<br>
•	Ağ simülasyonu, gerçek network paketlerini kullanma.<br>
•	Dağıtık sistem ya da çoklu işlemciler olan yapıları simüle edebilme.<br>
•	Simülasyonun sonucunda girdi, çıktı gibi olayları kaydetme.<br>

NS-3 kütüphanesi, bazı bileşenlerin birleşiminden oluşmakta. Bu bileşenler; çekirdek, simülatör, node(düğümler), araçlar, modüller ve ortak yaygın şeklindedir.

<br><br>

## 6.	Cisco Packet Tracer

Network'lerin (ağ'ların) nasıl çalıştıklarını inceleyebilmek ve üzerinde denemeler yapmalarına olanak sağlayan, Cisco firması tarafından geliştirilmiş olan bir ağ simülasyon programıdır.

<br><br>
 <img src="https://github.com/yilmazcelikk002/UygulamaProjesi/assets/132395836/63f18784-c892-4761-952b-280fd6332dc4" align="center" width="480" height="320">
 <br><br>
 
Kütüphanesinde sadece kendi firması olan CISCO’ya ait ürünler bulunmakta. Kablosuz erişim noktası, Yönlendirici, IP telefon sistemler anahtar vb. farklı türde araçlar kullanılabilmektedir. Yazılımın Windows ve Linux sürümleri bulunmaktadır. Program içerisinde sanal cihazlar oluşturulabilmektedir ancak reel hayat ile bağlantısı yapılamamaktadır. Klasik bilgisayar ağlarının yanında, üst katmanlarda da uygulama gerçekleştirilmesi mümkündür. Web sunucuları, DNS, e-posta sunucuları gibi servislerin simülasyonu sanal sunucu cihazı üzerinden gerçekleştirilebilmektedir.
<br><br>

## 7.	CORE (Common Open Resource Emulator) 
	
Sanal ağlar oluşturmak için kullanılan bir ağ simülatördür. Bir simülatör olarak CORE, soyut modellerin kullanıldığı simülasyonların aksine, gerçek zamanlı gerçek bir bilgisayar ağının temsilini oluşturmaktadır. Gerçek zamanlı simülasyon, fiziksel ağlara ve yönlendiricilere bağlanabilmektedir. Linux işletim sistemi tarafından sağlanan araçlardan yararlanmaktadır.

 
<img src="https://github.com/yilmazcelikk002/UygulamaProjesi/assets/132395836/e8c34bdd-1843-4544-ac5f-f2dd174e128f" align="center" width="480" height="320">
<br>

CORE genel olarak uygulama testi, platform testi, ağ araştırması, gösteriler, network oluşturma senaryolarını inceleme gibi işlemler için kullanılır. 
<br><br>

## 8.	GTNetS (Georgia Tech Network Simulator)
	
Georgia Tech Network Simulator ( GTNetS) mevcut ağ simülasyon araçlarının kolayca oluşturabileceğinden çok daha büyük ölçekli simülasyonlara izin verecek şekilde özel olarak tasarlanmış ağ simülasyon prgoramıdır. Simülatörün tasarımı, gerçek ağ protokolü yığınlarının ve donanımının tasarımına çok yakındır. Bu ağ simülatörü tamamen nesne yönelimli yapıda C++ programlama dili ile uygulanmıştır. 

GTNetS, Linux, OSX, Solaris ve Windows platformlarını desteklemektedir. GTNet'ler kullanılarak paketleri takibi, rastgele sayıların üretilmesi, sıralama yöntemleri, istatistiklere dayalı analitik yöntemler iyi bir şekilde analiz edilebilmektedir.
<br><br>

## 9.	NetSim (Network Simulator)

NetSim, hem basit hem de karmaşık ağ yapıları oluşturmak için geliştirilmiş ve bunu yanında verimliliklerini analiz etmek için kullanılabilecek pratik, kullanışlı ve güçlü bir ağ simülasyon programıdır. Sistem davranışı ve meydana gelebilecek sorunlarla ilgili bilgileri görüntüleyerek ağ güvenilirliğini değerlendirebilir.


 <img src="https://github.com/yilmazcelikk002/UygulamaProjesi/assets/132395836/d4cd222f-1986-42ed-9ea2-1b6923539229" align="center" width="480" height="320">
<br>

NetSim Network Simulator, klasik ev ağları, büyük ve kompleks yapıdaki ağları gerçekçi düzeyde oluşturabilir. Basit iş istasyonlarından sunuculara ve sensörlere, yönlendiricilere veya ATM anahtarlarına kadar her tür cihazdan oluşan çeşitli farklı konfigürasyonlarla kolayca ağ senaryoları oluşturulabilir.
NetSim, hem kablolu ağlar için hem de kablosuz ağlar için veri paketlerinin nasıl iletildiğini görmemizi sağlayan grafiksel entegre paket animatörüne sahiptir.
<br><br>

## 10.	Qualnet (Network Simulator)

Ölçeklenebilir ağ teknolojileri ile büyük ölçekli ve heterojen ağlar için bir Qualnet Ağ Simülatörü geliştirilmiştir. Her türlü veri, ses ve video ağları için ses modelleri oluşturmak için kullanılır. Gerçek zamanlı ağ simülasyonunu destekler ve temel olarak C++ ile yazılmıştır. 

<img src="https://github.com/yilmazcelikk002/UygulamaProjesi/assets/132395836/f89f1ebe-34f7-42e5-8497-d2ac78ca6fb2" align="center" width="480" height="320">
<br>

Microsoft Visual Studio  ile entegre olduğundan dolayı satır satır hata ayıklaması yapabilmektedir. Qualnet, gelişmiş grafik arayüz desteğine sayesinde XML kullanarak değiştirmenize veya yeni menüler/protokoller eklemenize izin vermektedir. Qualnet, Windows, Solaris, Linux, UNIX, Mac os işletim sistemi iler çalışabilmektedir.

<br><br>

# B.	MESAJ KUYRUK YÖNETİM SİSTEMLERİ

#### Mesaj kuyruğu(Message Queue, MQ) nedir?
Bir mesaj kuyruğu, iki hizmet arasında zaman uyumsuz(asenkron) iletişimi sağlamak için kuyruk veri yapısını kullanan bir mesajlaşma tekniğidir. Genellikle sunucusuz ve mikro hizmet mimarilerinde kullanılırlar.
<br>
Mesaj kuyruğu iki bileşenden oluşur:<br>
•	Mesaj : Göndericiden alıcıya iletilen veridir. İletin bu veri, bir istek, bilgi, meta veri vb. olabilir.<br>
•	Kuyruk :Gönderici tarafından iletilen mesajları depolayan ve sıraya alan geçici bir bellektir. Mesajları göndericiden alıcıya iletmek için FIFO(İlk Giren İlk Çıkar) yöntemini kullanır.<br>
<br><br>

## 1.	RABBİTMQ 

Açık kaynak(Open Source) kodlu bir mesaj kuyruk yönetim sistemidir. Bu sistem Erlang programlama dili ile geliştirilmiştir. Bağlı olmayan yani asenkron sistemler arasındaki bilgi alış verişini sağlar. Bir projede RabbitMQ desteği varsa projenin hangi dilde yazıldığının önemi çünkü; MQTT, HTTP ve AMQP gibi protokolleri desteklemektedir.

Farklı işletim sistemlerine kurulabilir ve kullanılabilir olması yaygın kullanımlı olmasını sağlayan etmenlerdendir. Web arayüz desteği bulunduğundan kullanımı kolaydır.

RabbitMQ, iletim zamanı uzun sürebilme ihtimali olan durumları uygulamadan bağımsız hale getirerek sorumluluğu üstlenip uygulamanın gecikme yaşamasının önüne geçmektedir.

<img src="https://github.com/yilmazcelikk002/UygulamaProjesi/assets/132395836/b4594e1a-ead0-40ad-b607-c1aac846b00d" align="center" width="480" height="320">
<br>

#### RABBİTMQ Temel Bileşenleri
Procedur (üretici), mesajı üreten taraftır. RabbitMQ ya publish eder.
Exchange, mesajı ilk olarak karşılayan yapıdır. Mesajın özelliklerine göre, ilgili mesajı hangi kuyruğa göndereceğine karar verir.
Consumer, Kuyruktaki işlemleri mesajları alan karşılayan yapıdır.

#### Genel Çalışma mantığı olarak; 
Producer:
1) Client kuyruğunda mesajı bekle
2) Mesajı al ve işlemi yap
3) Sonucu server kuyruğuna yolla


Consumer:
1) Server kuyruğunda kendine ait ID’li mesajı bekle
2) Mesajı al ve işlemi yap
<br><br>

##  2.	ZEROMQ (ØMQ, 0MQ, ZMQ)
ZeroMQ, eş zamansız/asenkron G/Ç modeli, size eş zamansız mesaj iletimi sağlamaktadır. Birtakım dil API'sine sahiptir. Birçok işletim sisteminde çalışır. ZeroMQ, karmaşık iletişim kararları geliştirmeye izin veren bir mesajlaşma kuyruğu sistemidir.  C++ programlama dili ile yazılmıştır. Açık kaynak kodlu bir mesaj yönetim sistemidir.

 <img src="https://github.com/yilmazcelikk002/UygulamaProjesi/assets/132395836/64713348-baeb-490e-82bc-ff9d39f9a627" align="center" width="320" height="140">
 <br><br>
 
Birden çok dil desteği bulunmaktadır. ( C, C#, C++, Erlang, Go, Haskell, Java, JavaScript, Perl, PHP, Python, Objective-C, Scala)
AT&T, Cisco, EA, Los Alamos Labs, NASA, Weta Digital, Zynga, Spotify, Samsung, Microsoft ve CERN gibi firmalar kullanmaktadır.
ZeroMQ motorlarının çoğu TCP kullanır.  UDP Tek Noktaya Yayın ve Çok Noktaya Yayın modlarını destekler.
<br><br>

## 3.	APACHE KAFKA
Apache Kafka, mesajların bir sistemden diğer bir siteme hızlı bir şekilde bir şekilde iletimini sağlamak için oluşturulmuş bir kuyruk yönetim sistemidir. İlk olarak 2011’de Java ile Linkedin tarafından giliştirilmiş ancak sonrasında Apache çatısı altında open source(açık kaynak) bir proje haline getirilmiştir. Devasa boyutlarda veriye sahip olduğu bilinen Netflixx Uber, Linkedin, Twitter gibi birçok firma tarafından kabul görmüş ve kullanılmaktadır.
Kafka, büyük veriden, ilişkisel veri tabanlarına, veri ambarlarından, NoSql gibi bilgi sistemleri arasındaki veri alışverişini sistemden bağımsız olarak yapılmasını sağlamaktadır. Hatta bu iletimi milisaniyeler seviyesinde yapar.


<img src="https://github.com/yilmazcelikk002/UygulamaProjesi/assets/132395836/ddfcdccc-b699-4d7c-9199-d6e64f2e6d1e" align="center" width="480" height="320">
<br><br>

#### Apache Kafka bileşenleri
•	Topic ve Partition: Topic verilerin gönderilip alındığı ksımdır. Kafka cluster’ında birden fazla topic olabilir. Topic’ler partition’lara ayrılırlar. Partition’lar 0’dan artan sayıda isimlendirilirler. Apache Kafkada bilgi belli bir süre tutulur örneğin 1 hafta gibi, daha sonra bilgi silinmektedir. <br>

•	Broker: Kafka Cluster’ı oluşturmakla görevli sunuculardır. Her brokera tanımlı bir ID bulunmaktadır. <br>

•	Producer: Mesaj göndermekle görevli bileşendir. Mesajı belli bir topic’e göndermektedir. Yayımcı gibi görev yapar. Mesajı topic’e gönderirken şki farklı yoldan gönderebilir. Bunlar key ile ve key’siz .<br>
•	Consumer: Consumer, Producerin gönderdiği mesajı okuyan bir bileşenidir. Abone/alıcı gibi düşünülebilir.<br>
•	Topic Replication: Sunuculardan birinin çevirim dışı olması durumunda sistemin devam etmesini sağlayan ve veri kaybını önleyen bileşendir.<br>
<br><br>

## 4.	Apache ActiveMQ(Active Message Queue)

Apache ActiveMQ, temelini Java Mesajlaşma hizmetinin(JMS) oluşturduğu mesaj yönetim yazılımıdır. Java dili ile yazılmıştır. Açık kaynak kodlu bir yazılımdır. Farklı platformlarda çalışabilmektedir. Kümeleme, JMS sunucusu üzerinden herhangi bir veritabanını  kullanma, mesajları önbellekte tutma, mesajları depolama, günlüğe kaydetme gibi birçok özellik sunmaktadır.

<img src="https://github.com/yilmazcelikk002/UygulamaProjesi/assets/132395836/ef478b6f-723d-4a1d-8f1b-9ac7fee32e95" align="center" width="320" height="140">
<br><br>

Birden çok dil desteği sunmaktadır (C#, C, C++, Erlang, Go, Haskell, Haxe, Jekejeke Prolog, NetLogo, Node.js, Perl, Pike, Python, Racket, Ruby on Rails). Farklı protokelleri de desteklemektedir(AMQP, AUTO, MQTT, OpenWire, REST, RSS ve Atom, Stomp, WSIF, WS Notification, XMPP, WebSocket).
Mesaj iletim şekli normalde varsayılan olarak eşzamanlıdır. Ancak birtakım ayarlamalar ile eş iletim sağlanabilmektedir. Eşzamansız iletim için ActiveMQConnectionFactory üzerinde useAsyncSend özelliği ayarlanabilir.
<br><br>

## 5.	 NSQ nedir?
NSQ, milyonlarca mesajı işleyerek geniş çaplı iletim ve işleme kapasitesine sahip açık kaynak kodlu mesajlaşma yönetim platformudur. Gerçek zamanlı olarak çalışmaktadır. NSQ, sunucu yeniden başlarsa ya da offline olursa bile mesajları bellekte tutmaya devam eder. Her mesaj en az bir kez teslim edilmesini garanti eder. NSQ, Go ve Python istemci kütüphanelerinin yanı sıra farklı dillerde kütüphaneleri de mevcuttur. 


<img src="https://github.com/yilmazcelikk002/UygulamaProjesi/assets/132395836/fa274883-82a6-4358-ab83-1b62b9f6e7f8" align="center" width="320" height="140">
<br><br>
NSQ Mesaj Kuyruk Yazılımı  3 bileşenden oluşur: <br>
•	NSQD, mesajları istemcilere ileten, mesajları arabelleğe alan bileşendir.<br>
•	NSQlookupd, istemciler, belirli bir konu için NQSD bileşenini keşfetmek için nsqlookupd'yi sorgular. NQSD ise yayın bilgilerini ve kanal bilgilerini yayınlar.<br>
•	NSQADMIN, yönetici görevleri için gerçek zamanlı bir web tabanlı kullanıcı arayüzüdür.<br>
<br><br>

## 6.	RocketMQ (Rocket Message Queue)<br>
RocketMQ, Alibaba Group tarafından geliştirilmiş olan profesyonel bir mesaj kuyruğu yönetimi yazılımıdır. RocketMQ, mesaj iletme, yayınlama, mesaj izleme, gecikme mesajı yönetimi, kaynak istatistikleri çıkarma gibi hizmetler sunmakatadır. 
RocketMQ Java, C++, .NET, Go, Python, Nodejs ve PHP'yi dillerini desteklemektedir. TCP ve HTTP protokollerini desteklemektedir. 
 <br><br>

 <img src="https://github.com/yilmazcelikk002/UygulamaProjesi/assets/132395836/34d3d209-c64d-45ab-ab5a-a1ebd886587a" align="center" width="320" height="140">
 <br><br>
 
#### RocketMQ'nun Avantajları<br>
•	RocketMQ farklı sistemler arasında veri tutarlılığını sağlar. <br>
•	Gecikmeli mesaj desteği sunmaktadır.<br>
•	İletimi başarısız olan mesajların, belirli sayıda ve zaman aralığında tekrardan gönderilmesi gibi önemli özelliğe sahiptir.<br>
•	40 güne kadar gecikmeli teslimatı destekler.<br>
•	4 MB'a kadar mesaj desteği sunmaktadır.<br>
•	İletim için gönderilen mesajları gönderildikleri aynı sıra ile alıcılara iletimini sağlar.<br>
•	Gönderilen mesajlardan iletilmemiş olanları, özel bir mesaj kuyruğunda saklayabilmektedir.<br>
<br><br>

#### RocketMQ’nun Bileşenleri:<br>
•	Web konsolu: Mesaj yönetimi, gönderici yönetimi, alıcı yönetimi, mesaj sorgularını, mesaj hareketlerini, raporlamaları ve alarm yönetimini gibi özellikler sunar.<br>
•	Açık Kaynaklı API: Kullanıcıların, RocketMQ yönetim araçlarını kendi sistemlerine dahil etmelerine sağlamaktadır.<br>
•	MQadmin komut seti: RocketMQ hizmetini yönetmek için etmek için geniş bir kod kütüphanesi sunar.<br>
<br><br>

## 7.	MSMQ (Microsoft Message Queue) 

MSMQ, dağıtık sistemlerde (aralarında sürekli bir bağlantı gerektirmeyen)
Güvenli bir biçimde iletişim kurulmasını sağlayan mesaj kuyruğu yönetim protokolüdür. MSMQ üzerinden kuyruğa mesaj gönderilir. Sistemde gelen bu mesaj, ilgili uygulama kuyruğa giderek kontrol eder ve kendisine gelen bir mesaj varsa gelen mesajı alır ve ilgili yere ulaştırır. Aşağıdaki şekilde iletim süreci gösterilmiştir.

<img src="https://github.com/yilmazcelikk002/UygulamaProjesi/assets/132395836/4d96c5b4-8aad-42fb-9870-6d39b2895927" align="center" width="480" height="320">
<br><br>

MSMQ, sayesinde bağımsız çalışan iki ayrı sistem birbirlerini etkilemeden, etkilenmeden mesajları alabilir ya da gönderebilir. Bu sayede sistemde çalışan birimlerden bir veya birkaçının devre dışı kalması durumunda sistemin normal işleyişine devam edebilmesine sağlanmaktadır. 

MSMQ teknolojisi, Windows işletim sistemi üzerinde hazır olarak gelmekte.  Ancak isteğe bağlı olarak açılabilen bir özellik şeklinde gelmektedir. Kişisel bilgisayar ve sunucu işletim sistemlerine için farklı farklı versiyonları bulunmaktadır.  
<br><br>

## 8.	IBM MQ
IBM tarafından 1993'te piyasaya sürülmüştür. Mesaj kuyruk yönetim yazılımıdır. İlk olarak MQSeries ismiyle anılıyorken, 2002 de WebSphere MQ olarak yeniden adlandırıldı. Ancak, 2014'te IBM MQ olarak şu anki adıyla kullanılmaya devam edilmekte.  IBM MQ, IBM MQ Advanced, IBM MQ Appliance, IBM MQ for z/OS ve IBM MQ on IBM Cloud'dur farklı versiyonları bulunmaktadır. 

IBM MQ, birbiri ile bağlantılı olmayan sistemlerde ve eşzamansız olarak çalışan uygulamalar arasında güvenli bir biçimde iletişim kurmalarını sağlar.  Diğer mesaj iletim protokollerinde olduğu gibi , depolama, yönlendirme ve teslim gibi bilgiler mesaj alıcıya iletilmeden önce eklenir ve alıcıya mesajı teslim almadan önce de mesajdan çıkarılır. IBM MQ, hem IBM hem de IBM dışı farklı platformlarda kullanılabilir.

#### IBM MQ’nun Temel Bileşenleri:<br>
•	Mesaj : Mesajlar, ikili(ASCII)  veya karakter(EBCDIC ) veri kümeleridir. <br>
•	Kuyruk : Gönderici tarafından gönderilen mesajların alıcıya ulaşana kadar depolayan birimdir.<br>
•	Kuyruk Yöneticisi : Mesajın alımından iletimine kadar her alan da sorumlu bileşendir. Ayrıca, depolama, zamanlama, tetikleme gibi mesajların hareketiyle ilişkili olmayan diğer işlevleri de yerine getirmekten sorumludur.<br>
<br><br>

## 9.	Amazon SQS (Amazon Simple Queue Service )

Amazon.com tarafından 2004 yılında kullanıma beta sürümü olarak sunulmaya başlanmış ve asıl olarak 2006 yılında tam olarak kullanıma başlanmış bir mesaj kuyruklama hizmetidir. SQS'nin amacı, gönderici ile alıcı arasındaki sorunlardan, bağlantı hatalarından kaynaklanan sorunları çözen, ölçeklenebilir mesaj kuyruk yönetim yazılımıdır.

Amazon,  Java , Ruby , Python , .NET , PHP , Go ve JavaScript gibi çeşitli programlama dillerinde yazılım geliştirme araçları sağlamaktadır. 

<img src="https://github.com/yilmazcelikk002/UygulamaProjesi/assets/132395836/8688c10f-5a11-42fe-9259-08dee0be1e6f" align="center" width="480" height="320">
 <br><br>
 
SQS ile gönderilen bir mesaj iletildikten sonra otomatik olarak silinmez. Bu mesaj teslim edildiğinde, mesaja “mesaj iletildi” anlamında bir ek oluşturulur ve alıcıya gönderilir. Bu ek mesajla birlikte değil, mesaja gönderildikten sonra arkasından gönderilir. Bir başka özellik ise tekrarlanan mesajları kaldırma özelliğidir. 

SQS için iki kuyruk yönetim yapısı vardır.<br>

#### Standart Kuyruklar<br>
Standart kuyruklar, eylem başına saniyede neredeyse sınırsız sayıda işlemi desteklemektedir.
Bir mesaj en az bir kez teslim edilme garantisi vardır, ancak bazen mesajların birden fazla kez gönderilme ihtimali vardır.
Bazen, gönderilen mesajlar gönderilişi sırasıyla aynı olmayabilirler.

#### FIFO Kuyrukları<br>
FIFO kuyrukları, saniyede 300 adede kadar mesaj alma, gönderme veya silme işlemini desteklemektedir.
Bir mesaj bir kez gönderilir ve teslim alınır ve alıcı o mesajı işleyip silene kadar kuyruk depolanmaya devam eder. Ayrıca birden fazla kez gönderilen mesajlar kuyruğa eklenmez.
Mesajların gönderilme sırası da ve alınma sırası da değişmez yani ilk gelen ilk alınır.
<br><br>

## 10.	gRPC (Google Remote Procedure Call)

gRPC, Google tarafından geliştirilmiş Remote Procedure Call, başka bir servis ya da uzak bir sunucudaki bir metodu sanki kendi servisimize ait bir metotmuş gibi kullanabilmesini sağlayan yazılımdır. İstemci sunucu ilişkisindeki iletişimi kolay ve hızlıca sunan bir frameworktür. gRPC, client-server arasındaki işlevleri yerine getirmek için REST yerine kullanılan bir iletişim protokolüdür. Bu işlevler, mobil uygulamalar veya CLI araçları olabilir. İstemci, sunucuya bir istekte gönderir ve sunucu ise bu isteğe yanıt verir.

 <img src="https://github.com/yilmazcelikk002/UygulamaProjesi/assets/132395836/fa691b3e-49ae-4b0c-a502-91aa3e5989db" align="center" width="220" height="100">
 <br><br>
gRPC, açık kaynaklı ve yüksek performans sunan bir Uzaktan Yordam RPC çerçevesidir. gRPC istemcileri ve sunucuları, gRPC'nin desteklediği herhangi bir dilde yazılabilmektedir. Go, Python veya Ruby programlama dilleri ile istemcileri, Java'da ise gRPC sunucusu oluşturulabilmektedir. gRPC bir RPC gibi düşünülebilir ancak bu yaklaşımın yeni bir versiyonudur ve çok çeşitli özellikler ekler.<br><br>

gRPC'nin eklediği en büyük özellik protobuf kavramıdır . Protobuf, verileri serileştirmek için kullanılan dillerden ve platformdan bağımsız yapılardır. Ayrıca gRPC, Google'ın çok etkili ve güçlü bir kimlik doğrulaması olan SSL/TLS sistemine sahiptir. gRPC ayrıca açık kaynaklı bir yazılımdır. Github for C, C++, Java, Node.js, Python, Ruby, Go, C#, PHP, Objective-C gRPC core gRPC java gibi dillerle kullanılabilmektedir.


