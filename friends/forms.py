
from flask_wtf import FlaskForm

from wtforms import StringField, SelectField, BooleanField, HiddenField
from wtforms.validators import DataRequired

class FriendForm(FlaskForm):
    
    name = SelectField('Name:', validators=[DataRequired()],
        choices=[
            ('Joey'),
            ('Chandler'),
            ('Rachel'),
            ('Ross'),
            ('Monica'),
            ('Phoebe')
        ]
    )
    image = SelectField('Image:', validators=[DataRequired()],
        choices=[
            ('1.gif', 'Joey'),
            ('2.gif', 'Chandler'),
            ('3.gif', 'Rachel'),
            ('4.gif', 'Ross'),
            ('5.gif', 'Monica'),
            ('6.gif', 'Phoebe')
        ]
    )
    invited = BooleanField('Invite friend to the party.')

class EditFriendForm(FriendForm):
    id = HiddenField(validators=[DataRequired()])

class DeleteFriendForm(FlaskForm):
    id = HiddenField(validators=[DataRequired()])