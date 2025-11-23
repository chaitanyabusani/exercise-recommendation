from flask import Flask, request, render_template


import pickle



file1 = open('bodyfatmodel.pkl', 'rb')
rf = pickle.load(file1)
file1.close()


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        my_dict = request.form

        density = float(my_dict['density'])
        abdomen = float(my_dict['abdomen'])
        chest = float(my_dict['chest'])
        weight = float(my_dict['weight'])
        hip = float(my_dict['hip'])

        input_features = [[density, abdomen, chest, weight, hip]]
        prediction = rf.predict(input_features)[0].round(2)

        # <p class="big-font">Hello World !!</p>', unsafe_allow_html=True

        string = 'Percentage of Body Fat Estimated is : ' + str(prediction)+'%'
        if prediction>50:
            recommendation = "Workout is needed to reduce body fat do following exercise High-Intensity Interval Training (HIIT), Running/Incline Running, Cycling, Jump Rope, Swimming, Weightlifting exercises like deadlifts, squats, bench presses, and kettlebell swings."
        else:
            recommendation = "Just do normal exercise to maintain body fat, so do following execises Walking, jogging/running, Push-ups, squats, lunges, and planks, Stretching."
        return render_template('show.html', string=string,
recommendation=recommendation)

    return render_template('home.html')


if __name__ == "__main__":
    app.run(debug=True)
