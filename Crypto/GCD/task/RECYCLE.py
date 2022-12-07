from Crypto.Util.number import bytes_to_long
flag=open("flag.txt","rb").read()

pubkey=[2611174833305801825594730778254837997519349014267876004669610898687852191138081308805218785523866930303179794791100636991564474137820221540449788073320666790785292133289917794963785069804681451944541217856866903789142094418627671327106897656920554136167286159023868344788900379082283440169572765508823303507196103441452762209167510019015026477194879188811694153836737262010875215668622782212961576924611037589100897985584733881088119204215542152734303241007455028176654213104335471457752964990368365025178510346101287791454206213937606462392412305962779013644610855161520412392889136412653616254759340413002158463410486102932695275696678572630715367818929025185116223041854793194275805191775971335394831257013040452400425577599220088526219843765446136535307476089944244418880269267659583905365045667258457118252722599886661841857781275629, 3710087729197168755663271382765696204364843712831250265391958563958267720405634930798878485744462982752012325622621235210519983713521803471697371910581509, 2411675554693636284265527358753316566737971629882522722750572585797475693459977119936006461181527401293175066232017139831144054293107260552973376574533278484145269366968515681870118970087958892480550963341003557704852148364185972586811188243198724356230073124794637472591127643110257595791443713757585664389508386929351912171628727347436000170747596005449745254783585231424815535758157035471550709613656477106051484984524070139917017627672704426830401849446097323570406583583601775760155595908109741446782245823654291200468152082095339833566092094855864981827504327107178335581002757914749425082323102652842253797298442916570488589518017809684355876242453401916873660875256010546639883719194977884251898152567677765015514025268051646530244625162108060547746118311242121177948585771580564342211971532046072690436406032133715247099239120903, 6833298622578542188030002349438967031074373206485294852093409802953458868524752632700463715068611912569328320271081099422915312130193684389377673539631187, 12072724589614093455615722188943027533113015065620729987695836638978097748199878606652945607883958997291844407703815001289473034874989613238136541321045389, 4434236564213975563236476109134913392910353293015339798019880754299190694903731002971773501889490490992161754435593764505128722427025246648638081269474301, 3974694704228068753094533108174599565527788519925190598046373623528871897397488814637588317950553018845730903439467729412962995757945600257308000656844379, 7067346678906598734810771382007194364664106574625814087853417114667312620033878502699619287178221470456535931334259633379856888315406307981769952802035983, 6598228988241185778262123469056490874169856972329461903433956956814289948448544935830513127924797748383144730631304085397564388431775908853794453526004689, 7749622564206620496017051929128847386259408314844953094206169431598565479928386122777936286230145313031486751837175387610104665742182716139156427892179773, 6460106832269242615740890218941373948198489897124429405004811646206531451300409442484800437484408119410834891856100106543049827086463084738954620940535383, 4863525562533465317523122988823796772397295249520086083468526236938487558395331633655832100077401918057664741263659072693521218665316831470684552281240317, 11012937152220534083755930181509673034253255024047955161010237358449844512115689402004972385674193390453197941286033354947606716916419926786757868726447471, 3954049896505725355430578934567878139708319614129134249311534714442433495698412086661368575687996391754480412479325024241059005183320951237834157471211227, 4895373129567506989709619396213251512056041322283781294364225232771906534787637732776246743869244312745880649236183326272305274802657223376335067304531821]
ciphertext=[]
e=0x1001
ciphertexts=[pow(bytes_to_long(flag),e,i) for i in pubkey]
print(ciphertexts)