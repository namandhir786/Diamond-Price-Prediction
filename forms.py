from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class DiamondForm(FlaskForm):
    carat = StringField('Carat', validators=[DataRequired(message="Please enter a carat value.")])
    depth = StringField('Depth', validators=[DataRequired(message="Please enter depth value.")])
    table = StringField('Table', validators=[DataRequired(message="Please enter table value.")])
    x = StringField('X', validators=[DataRequired(message="Please enter x value.")])
    y = StringField('Y', validators=[DataRequired(message="Please enter y value.")])
    z = StringField('Z', validators=[DataRequired(message="Please enter z value.")])

    cut = SelectField('Cut', choices=[('Fair', 'Fair'), ('Good', 'Good'), ('Very Good', 'Very Good'), ('Premium', 'Premium'), ('Ideal', 'Ideal')],
                      validators=[DataRequired(message="Please select a cut.")])
    
    color = SelectField('Color', choices=[('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J')],
                        validators=[DataRequired(message="Please select a color.")])
    
    clarity = SelectField('Clarity', choices=[('I1', 'I1'), ('SI2', 'SI2'), ('SI1', 'SI1'), ('VS2', 'VS2'), ('VS1', 'VS1'), 
                                              ('VVS2', 'VVS2'), ('VVS1', 'VVS1'), ('IF', 'IF')],
                          validators=[DataRequired(message="Please select a clarity.")])

    submit = SubmitField('Submit')