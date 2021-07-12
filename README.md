# Rüya tabiri telegram botu

Rüya tabiri yapan bir telegram botu için adım adım öncelikler anlatılmış ve kodlar paylaşılmıştır. Hem telegram botu yapma konusuna hem de rüya tabiri yapan yapay sezgi geliştiren bir bot yapımı için nelerin gerektiğini ve nasıl yapmanız gerektiğini gösteren kodlarımla sizlerin de benzer botlar yapabileceğini düşünüyorum.

## Telegram ve Python kodu

Öncelikle Telegramdan bir bot sahibi olmalısınız. Bot sahibi olmak için @BotFather botunu ekleyip yönergeleri takip etmelisiniz. Karşılığında bir botunuz ve ona ait token elde etmiş olacaksınız.

Python programlama bilgisi de biraz gerekiyor. Telegram bot için python programlama dışında programlar da kullanabilirsiniz ama şimdi burada python için olanı açıklayacağım. ruyarabot kaynak dosyasında bottan gelen tokeni yazınız. İçeriği istediğiniz gibi değiştirebilirsiniz. 

25. satırdaki 

```
def echo(update, context):
    with open("sayac.txt","r") as dosya:
        sayac=int(dosya.read())
    sayac+=1
    with open("sayac.txt","w",encoding="utf-8") as dosya:
        dosya.write(str(sayac))
    """Echo the user message."""
    update.message.reply_text(cevap(update.message.text)) #cevap yani tabir üreten modüle yönlendiriyoruz
```

Bizim rüya tabiri üreten modüle yönlendiriyor. (buradaki sayaç dosyasını ben ekledim, kaç kişinin rüya tabiri sorduğunu bulmak için her tabir soruluşta sayacı bir arttırıyor. Eğer istatistik kısmına meraklı değilseniz bu kısmı silebilirsiniz.

Şu an çalışan bir uygulamasını görebilirsiniz: https://t.me/ruyarabot
