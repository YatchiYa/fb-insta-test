
# define db url to connect 

# local db
#db_url = 'mongodb://localhost:27017/'

# server db on atlas mongodb (defined on Amazon cloud)
db_url = 'mongodb+srv://' + 'yatchiAuth' + ':' + '1y2o3u4e5f' + '@' + 'skybreaker01' + '-gcpvn.mongodb.net/test?retryWrites=true&w=majority'

# define the instagram api key
api_key = {   
    # define the instagram api key  
    'insta_api_key' : "81bd064f38msh8bbe65cd1eac9ccp11bb0ajsn8974f1eae7df",
    # facebook api token 
    'token_fb': "EAAGZAhN3OgkMBAF5bEZAIMko0QXvXWbOi5U19oSTFqyDE6QSwyhIzGhazzwwZAQPqIeIoLhNMtmuypQtAn0lSxIS3LqSIeQsv3cM003D2BivQxiKEkj2MoTRsKzYG0rPZCZCKYZAsnTgdQC4tJsrhijWxHJ4gZCa3KiZBQs6ZBhr8WIHFLUlBszXb"
}

dictonnary = ["rip","death","mort","aurevoir","au revoir","à dieu","triste","écroulement","agonie",
                "anéantissement","ankylosé","apathique","épuisé","éreinté","assassinat","éteint","évanoui","brisé",
                "cadavre","camarde","chute","claqué","condamné","corps","crève","crevé","croupissant","décédé",
                "décès","deces","décomposition","défunt","délavé","dépouille","désert","détruit","de cujus","dernier jour",
                "dernier sommeil","dernier soupir","destruction","deuil","disparition","disparu","dormant",
                "effondrement","enterrement","enveloppe","esprit","esquinté","euthanasie","exécution","excédé",
                "exténué","extinction","fade","fantôme","faucheuse","feu","fichu","figé","fin","fini","flapi",
                "fossoyeuse","foutu","grand voyage","harassé","immobile","inanimé","inerte","inhabité","insensible",
                "irrécupérable","ivre","languide","la Parque","lessivé","macchab","macchabée","malemort","mânes",
                "meurtre","morne","mortifié","morts","mourant","néant","nécrosé","nuit éternelle","ombre","parque",
                "passé","perdu","perte","plat","plongeon","rétamé","recru","rendu","repos","repos éternel","restes",
                "rompu","ruine","silencieux","sommeil éternel","somnolent","spectre","stagnant","supplice","terne",
                "tombe","tombeau","torture","tranquille","transi","trépas","trépassé","tué","usé","victime","vidé"]

#This is the hashtag we will search for in the Instagram API
hashtag = "presidentjacqueschirac"