import math


def check_coprime(e, phi_n):
    if math.gcd(e, phi_n) == 1:
        return True
    else:
        return False


# Example usage:
e = 12476887212021993442110199358752708924701803529059621093175425622733669467883949947675691475234619840011834907311190217746675989939216650576888857297178001403056607788173793659721519220407882836961485677701159975750390138203851217402392454956005136742255031959890511956859557608720511520058853969357120864446881543218382526647078638709071460669057484987187411974923404489695748418478767371507593607813077469421533128726917169213528495535265695658025714101916940969259166800885637644191776796994966368736184684887140181414647161683450038419593746287816314338161257353997108257593617988524369362310588581266068939675326027669497114879679046038423151758563663992545459471708675025023159091918738054836312530096887116627576765886836332242384589550677760173524776401596166561048772007836660782542723137806002228329694821136437125248879104380878605346854064161270003699426713321418697952142790909039713593442343136585458253528395537953163968403727546715054084005501503972372937126857768774412426981166583498541172324894492507227939862487991874328502902724366716535471281434150957384078323796582302111849142771371661806255270473692274380949379349855641011364277002743833951136056247725430654018957290228667

phi_n = 22197627184753288038457974711328048798864647862032004618632466596519657850270860930936499264174490258298744666401357865511739159026356819940792933313514576667874731277703691515605280190034636957578241292162921442114841046486098059261359473348342118147774534125872024640160049515453020006628337623688540506000557377922540333530314899046821417658216693134780719663358490087556941906748195569922983429590699113550223329060609550832900512714622582152321672643904178329139483724071685938113467459310279330329285814763794033483265498109170179428866503435903561250439253814024633886639788000047344300955503306765557498525616129794853341928322827817214982837313956944279383249929521882881232745486974727807879297914430079992535353367916411192471694184861946131794407684383060947337892086814435163924582781614899615986868425300125648407524358924244482700221149302257143312165525338049249789981031593179790590034346309306334213281385667208533942607548717203681683691692538964021361182140831262154232091570797305972564781079765859469874325757643241581692038556422206087201733279003222171590372005976612338189064033227846143358293805129795201179602069160077801679196037764135513508661495881258094962404010029920

is_coprime = check_coprime(e, phi_n)
print(is_coprime)
