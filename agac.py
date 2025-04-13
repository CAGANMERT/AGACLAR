import discord 
from discord.ext import commands
import os
os.makedirs("./fotograflar", exist_ok=True)
intents = discord.Intents.default()
intents.mesagge_content=True

from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np

def get_class(model_path, labels_path, image_path):

    # Disable scientific notation for clarity
    np.set_printoptions(suppress=True)

    # Load the model
    model = load_model("C:\Users\dell\OneDrive\Masaüstü\AI BOT\keras_model.h5", compile=False)

    # Load the labels
    class_names = open("labels.txt", "r").readlines()

    # Create the array of the right shape to feed into the keras model
    # The 'length' or number of images you can put into the array is
    # determined by the first position in the shape tuple, in this case 1
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    # Replace this with the path to your image
    image = Image.open("<IMAGE_PATH>").convert("RGB")

    # resizing the image to be at least 224x224 and then cropping from the center
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

    # turn the image into a numpy array
    image_array = np.asarray(image)

    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

    # Load the image into the array
    data[0] = normalized_image_array

    # Predicts the model
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    # Print prediction and confidence score
    print("Class:", class_name[2:], end="")
    print("Confidence Score:", confidence_score)

bot = commands.Bot(command_prefix="?", intents=intents)

@bot.command()
async def hangisi(ctx):
    try:
        if ctx.message.attachments:
            file_name = attachment.filename
            await attachment.save(f"./{file_name}")
            result = get_class("keras_model.h5", "labels.txt", f"./{file_name}")
            await ctx.send(result)
        else:
            await ctx.send("Dosya gördermezseniz maalesef yanıt veremem.")
    except UnicodeDecodeError as e:
        await ctx.send(f"Dosya kodlama hatası:"{e})
    except Exception as e: 
        await ctx.send(f"Bir hata var!:"{e})

async def mese(ctx):
    await ctx.send("Kayıngiller ailesinden olan meşe ağacı 400'ün üstünde türü olan yaprak döken ya da her zaman yeşil olan ağaçlardır. Çok büyüyen ve uzun ömürlü ağaçlardır. Meşe ağacının meyvesi palamuttur. İçindeki pelit maddesi sincap ve alakarga için önemli bir besin kaynağıdır.20 ila 30 m veya daha yükseklikte, gövdesi 2 m çapında, tacı gençlikte konik yaşlandıkça genişleyen bir orman ağacıdır. Yaprak : 6-12 x 3–5 cm boyutundaki 5-9 çiftli loplu yaprakların sinüsleri (boşluk) orta damara kadar uzanır veya ona yakın bir yerde sonlanır. Koyu yeşil yaprakların üzeri pürüzlü ve yıldız tüylüdür.")

async def cam(ctx):
    await ctx.send("Yaprak dökmeyen tek ağaç türü olan çamlar diğer ağaçlar gibi sonbaharda yaprakları taze durur ve yaz kış hep yeşildir. Bir diğer özelliği ise uzun ömürlü ve dayanıklı olmasıdır. Ayrıca iğneleri ve kendi ürünü olan kozalağı bulunur. Dayanıklı yapısı sayesinde her iklimde yaşayabilir. Çoğu çam, yangına uyarlanmıştır, yani yangının tekrarlaması, çamların, çam olmayanların hakimiyetine yol açan orman dizilerinde baskın bir rol sürdürmesine izin verir. Bu yangına adaptasyonun kesin doğası, bazı çamların sık sık düşük yoğunluklu yangınlara tolerans göstermesi ve diğerlerinin, meşcereleri yok eden yangınlara izin veren yüksek yakıt birikimleri üretme eğiliminde olması ve ardından çamların hızla yenilenmesiyle büyük ölçüde değişir. Ateşin seyrek olduğu veya hiç olmadığı habitatlarda, çam ağaçları serpantin çorakları, litosoller veya bataklıklar gibi besin açısından fakir yerlerde bulunma eğilimindedir. Düşük gölge toleransları tipik olarak kapalı bir orman gölgesinin altında büyümeyi engeller. Birçok tür çok kuraklığa toleranslıdır.")

async def ladin(ctx):
    await ctx.send("60 m bazen daha fazla boylanabilen ve 2 m'den fazla çap yapabilen düz ve dolgun gövdeli bir ağaç türüdür. Nemli havaları, derin, havalanma kapasitesi yüksek, nem içeriği fazla, kumlu ve balçık, besince zengin, humuslu serin toprakları sever. Böyle yerlerde çok iyi bir gelişme gösterir.Ladin, dayanıklı kağıt yapmak için birbirine bağlanan uzun ağaç lifleri olduğundan, kağıt yapımında en önemli ağaçlardan biridir. Lifleri ince duvarlıdır ve kuruduktan sonra ince bantlara çöker. Ladinler, kolayca ağartılır olduğundan mekanik hamurlaştırmada kullanılır.")

async def hus(ctx):
    await ctx.send("15-20 m boylanabilen, yazın yeşil, düzgün gövdeli, ağaç veya ağaççıklardır. Gövde kabuğu düzgün veya yırtılmış olarak görülür. Beyaz veya boz esmer renklidir. Dallar ince ve narin kızıl kahve renkli, yapraklar normal olarak dizilmiş, kenarları ince veya kaba dişli ya da lopludur.")

async def sakura(ctx):
    await ctx.send("Sakura kiraz çiçeği, bakımı kolay olan ve birçok yerde yetiştirilebilen bir bitkidir. Meyvesiz bir kiraz ağacıdır ancak görüntüsüyle büyüleyen özel çiçeklere sahiptir. Yaklaşık 8 ile 10 metreye kadar uzayabilen ağacın çiçekleri çok kısa sürede dalından düşer.")

async def akasya(ctx):
    await ctx.send("Akasya ağaçları ılıman iklimlerde kolay yetişen bir bitkidir. Ancak soğuğa ve kuraklığa dayanıklı olduğu için birçok bölgede yetişir. 600'den fazla çeşidi vardır. Baklagiller familyasından bir bitki olup yeşil yapraklıdır. Türüne göre beyaz, kırmızı ya da sarı renkli çiçekler açar.")

bot.run("TOKEN")
