from flask import Flask,render_template, request 
from tensorflow import keras
import random
from tensorflow.keras.models import Model
from tensorflow.keras.models import load_model

model = load_model("final.h5")

app = Flask(__name__)

@app.route("/predict", methods=['POST', 'GET'])
def upload():
    if request.method == "POST":
        cuisine = request.form.get('cuisine')
        print(cuisine)
        calories = request.form.get('calories')
        allergy = request.form.get('allergy')
        types = request.form.get('types')
        spicy = request.form.get('spicy')

        if cuisine == 'American':
            cuisine1 = 0
        elif cuisine == 'Indian':
            cuisine1 = 1
        else:
            cuisine1 = 2


        if calories == 'l200':
            calories1 = 0  
        else:
            calories1 = 1


        if allergy == 'peanuts':
            allergy1 = 0
        elif allergy == 'lactose':
            allergy1 = 1
        else:
            allergy1 = 2


        if types == 'veg':
            types1 = 0
        elif types == 'nveg':
            types1 = 1
        else:
            types1 = 2

        if spicy == 'l':
            spicy1 = 0
        elif spicy == 'm':
            spicy1 = 1
        else:
            spicy1 = 2


        

        # cuisine1 = float(cuisine)
        # calories1 = float(calories)
        # allergy1 = float(allergy)
        # types1 = float(types)
        # spicy1 = float(spicy)

    # if cuisine == 'italian':
    #     cuisine = 0
    # elif cuisine == 'american':
    #     cuisine = 1
    # else:
    #     cuisine = 2

    
    # if calories == ''

        price = [400,300,230,210,450,260,120,230,320,400,300,230,210,450,260,120,230,320,400,300,230,210,450,260,120,230,320]
        COLS_USED = ['peanut_butter_and_honey_toast', 'peanut_butter_and_jelly_smoothie',
        'Thai_peanut_stir_fry', 'broccoli_cheddar_soup', 'creamy_avocado_pasta',
        'spicy_cauliflower_mac_and_cheese', 'grilled_cheese_sandwich',
        'caesar_salad_with_grilled_chicken', 'shrimp_scampi', 'aloo_paratha',
        'rajma_chawal', 'cholle_bhature', 'biryani', 'dal_makhani',
        'shahi_paneer', 'dal_chawal', 'butter_chicken', 'pav_bhaji',
        'caprese_salad', 'minestrone_soup', 'pasta_with_marinara_sauce',
        'arrabbiata_pasta', 'puttanesca_pasta', 'pasta_allamatriciana',
        'diavola_pizza', 'spaghetti_alla_puttanesca', 'penne_allarrabbiata']
        


        prediction = model.predict([[cuisine1, calories1,allergy1,types1,spicy1]])
        pp = [1 if x >= 0.5 else 0 for x in prediction]
        zipped = zip(pp,price,COLS_USED)
        x = list(zipped)
        zipped_list_sorted = sorted(x, key=lambda x: x[0], reverse=True)
        items,price_list,product = zip(*zipped_list_sorted)
        item1,item2,item3,item4,item5,item6,item7,item8,item9,item10,item11,item12,item13,item14,item15,item16,item17,item18,item19,item20,item21,item22,item23,item24,item25,item26,item27 = product
        p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18,p19,p20,p21,p22,p23,p24,p25,p26,p27 = price_list

        print(item1,p1)
        return render_template("order.html", a=item1,b=item2,c=item3,d=item4,e=item5,f=item6,g=item7,h=item8,i=item9,aa=item10,bb=item11,cc=item12,dd=item13,ee=item14,ff=item15,gg=item16,hh=item17,ii=item18,aaa=item19,bbb=item20,ccc=item21,ddd=item22,eee=item23,fff=item24,ggg=item25,hhh=item26,iii=item27,
                            pp1=p1,pp2=p2,pp3=p3,pp4=p4,pp5=p5,pp6=p6,pp7=p7,pp8=p8,pp9=p9,pp10=p10,pp11=p11,pp12=p12,pp13=p13,pp14=p14,pp15=p15,pp16=p16,pp17=p17,pp18=p18,pp19=p19,pp20=p20,pp21=p21,pp22=p22,pp23=p23,pp24=p24,pp25=p25,pp26=p26,pp27=p27)
        # return render_template("about.html", msg = cuisine1) 


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/form')
def form():
    return render_template("form.html")

@app.route('/order')
def order():
    return render_template("order.html")
    

if __name__ == '__main__':
    app.run(debug=True)