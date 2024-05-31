from Crypto.Util.number import long_to_bytes
from sympy.ntheory.modular import crt

# Given values
n_values = [
    104866610138096401896130952235783709525020317357871338154021111465205959907135862488846912073876863050660155635596876730347895456144692615069259840859881371169084838308281043524214129308936537463499847322023548208230530268781672688533745438933642923401652502392146593260382662073996287591813207689199716408617,
    99432920987038651729166881092442996920596610198502696919029367414047553298918814788144343240906215727069424048165837639608080529721809737589511983199126346373654370098935363603303317905934579665965071385723675055197964654374062668885066796261210169675052496622377605308657673994922529397221183228667901632401,
    82644199792161634607383174114412537069016987281048080877751938988847004102634779549636734138597821988926621224504181453147995354397929293684139833158209790899463721652141655990616441490678271824835496992169795218909388715195132531009306624677079828782711880702549818277491117895925684080764066765890795274693,
    90724021823359180159866636798385172012897984988372851800856548732829961603851924238273906783403809254470708133742048732405841991509973663850166490233052093008748340382859240899175123300947691272667950715351985296935446297375124185604332984847621063974568059510946064903347786700087494876049137998967737336517,
    103467796750849375989169022653165534069147097723458088283059147354848827646222326147055712394159357676366991448727604622111596635717618493307532294622514451430107787572034060739434720045838570000318969045100853722766314097836954786528062123386251211430718668718047366345315455176762631621461170144231903018737
]
e = 3
c_values = [
    65277760183162330067603749041968151181134766691328197228918222217777798077846301882056962835357958181555192311261480709389582042389341911504395250493227497850756994120133144938453608236704274784554911351723680221323221426753591335581542840777059536248745306181526348000989527031227257808966511235600309148249,
    93279834071120729406462351904206713428255148614851288078232100448766338452465360208153470189364599470684067197191119911175676127815224111828033332808798295888502360574887020174469161532052292072807787835860129364824953000630557835389359585340020794311677204027539929632911696272300126343343843018610397458935,
    33418265633885181219979098097692247420926261993447856565692595707746591952433727806381479359136462671388428412047645963764903732237649606326854065547583908606873675537743982765880518589554591797538664351596551096382986747646951629757796429502146147214929360658228255492601778323943526366869929541554560998094,
    87402734777413287907370894231444079118901363686748130230511857362467167814941627608257338706571738600768514326583379301517644580972430148815590858109076835402676177573701838075326753683139474773531404386481487918353051989065922960638371484807691691523365172207926678006156386918243071371239091987166220994120,
    75549220368910009348406671152230485942595708595825065028033254622309347271025160571830145284752022015388043006489350609414546835665942726513284004414042752033890076714535981281011297701836196947595712383824954945214707332262605332534621254000718874793576632430247056379292092411676636525824811519692451621935
]

# Compute the cube roots modulo each n
val = 1/e
m_values = [pow(c, val, n) for c, n in zip(c_values, n_values)]

# Reconstruct the original plaintext using CRT
m, _ = crt(n_values, m_values)

# Convert the plaintext to bytes
plaintext = long_to_bytes(m)

print("Original plaintext:", plaintext.decode())
