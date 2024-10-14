from flask import Flask, request, render_template, jsonify
from src.pipelines.prediction_pipeline import CustomData, PredictPipeline
from forms import DiamondForm  # Import the DiamondForm class

application = Flask(__name__)
app = application

# Set a secret key for form validation (required by Flask-WTF)
app.config['SECRET_KEY'] = 'diamond-1'

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict_datapoint():
    form = DiamondForm()  # Create an instance of DiamondForm

    if request.method == 'POST' and form.validate_on_submit():  # Handle form validation
        data = CustomData(
            carat=float(form.carat.data),
            depth=float(form.depth.data),
            table=float(form.table.data),
            x=float(form.x.data),
            y=float(form.y.data),
            z=float(form.z.data),
            cut=form.cut.data,
            color=form.color.data,
            clarity=form.clarity.data
        )

        final_new_data = data.get_data_as_dataframe()
        predict_pipeline = PredictPipeline()
        pred = predict_pipeline.predict(final_new_data)
        results = round(pred[0], 2)

        return render_template('form.html', final_result=results, form=form)

    return render_template('form.html', form=form)  # Render the form even if it doesn't validate

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
