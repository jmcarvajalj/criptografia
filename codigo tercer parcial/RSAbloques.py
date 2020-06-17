#m a la e modulo n
#n = p*q
def power(x, y, p):
    res = 1  # Initialize result

    # Update x if it is more
    # than or equal to p
    x = x % p

    if (x == 0):
        return 0

    while (y > 0):

        # If y is odd, multiply
        # x with result
        if ((y & 1) == 1):
            res = (res * x) % p

            # y must be even now
        y = y >> 1  # y = y/2
        x = (x * x) % p

    return res
#PARA CIFRAR
m=82
e=65537
n=100802961127774615062574440190212595458415981340234147156257003202665895355972825947836959831817528640914072425145452188431670544915277664705142054141649605286654872822540542638414545513836754330075415328576191690067619244242360951970623753139863567471623475853050026733807966735089326615454946277680841398727
c = pow(m, e, n)
#verificacion por un metodo
print("Cifrado es",c)
#verificacion por otro metodo
print("Cifrado es",power(m, e, n))


#PARA DESCIFRAR
c=32672397227446388428666978489734236857112898592644984590083994383445695655192815968219479177953024247091415859044003432870237270261117434863394913045045802567807084277410771607289202306246015365413741133244248183148603700660464900382639783615039263561829257196071300744605793671281529328944406984361922906866
d=36511599420954786034688680611490708927657331965980716010730255306542609883883652629045481979457169154493160370906552696171490843267144684754728810919243752970969043571502056548634360800545481693397231222136952364317629124997679833838630393434837918712366848952337635243089906717156832296667070716570057498017
n=100802961127774615062574440190212595458415981340234147156257003202665895355972825947836959831817528640914072425145452188431670544915277664705142054141649605286654872822540542638414545513836754330075415328576191690067619244242360951970623753139863567471623475853050026733807966735089326615454946277680841398727
m = pow(c, d, n)
#verificacion por un metodo
print("Mensaje es",m)
#verificacion por otro metodo
print("Mensaje es",power(c, d, n))

