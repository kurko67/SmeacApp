from flask import render_template, request, jsonify, send_from_directory
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView, ModelRestApi
from .models import Form
from config import SQLALCHEMY_DATABASE_URI, basedir
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
import json
from . import appbuilder, db
from docxtpl import DocxTemplate
import os
from flask_cors import CORS, cross_origin

CORS(appbuilder.app)

class FormApi(ModelRestApi):
    datamodel = SQLAInterface(Form)

appbuilder.add_api(FormApi)


class FormView(ModelView):
    datamodel = SQLAInterface(Form)
    list_columns = ['id','created_at']
    show_fieldsets = show_fieldsets = [
        ('Details', {'fields': ['firstctrl1', 'firstctrl2','firstctrl3','firstctrl4', 'firstctrl5', 'firstctrl6', 'firstctrl7', 'firstctrl8', 'firstctrl9', 'firstctrl10','firstctrl11', 'firstctrl12', 'firstctrl13' ,
                                'secondctrl1','secondctrl2','thirdctrl1','thirdctrl2','thirdctrl3','thirdctrl4','thirdctrl5','thirdctrl6','thirdctrl7','thirdctrl8','thirdctrl9','thirdctrl10','thirdctrl11','thirdctrl12',
                                'thirdctrl13','thirdctrl14','thirdctrl15','thirdctrl16','thirdctrl17','thirdctrl18','fourtctrl1','fourtctrl2','fourtctrl3','fourtctrl4','fourtctrl5','fourtctrl6','fivectrl1','fivectrl2',
                                'fivectrl3','fivectrl4','fivectrl5','fivectrl6','fivectrl7','fivectrl8','created_at']}),
    ]
    label_columns = {
        'firstctrl1':'Describes the nature of the company’s business (manufacturer, operator, system integrator, etc.)',
        'firstctrl2':'Defines their geographic operating boundaries (lack of specifics implies very broad NAS access)',
        'firstctrl3':'Describes whether they will launch/fly/recover only over private property with owner’s permission',
        'firstctrl4':'Defines the minimum and maximum operating altitude of the vehicle',
        'firstctrl5':'Intends to operate within or beyond Visual Line of Sight (VLOS)',
        'firstctrl6':'Adequately defines command and control link',
        'firstctrl7':'Supplies information on dimensions, materials & processes necessary to define the vehicle design',
        'firstctrl8':'Identifies the congestion of their proposed operating area',
        'firstctrl9':'Identifies the vehicle’s maximum cruise speed',
        'firstctrl10':'Describes Their Proposed Airspace Classes (A, B, C, D, E, G, F, etc.)',
        'firstctrl11':'Defines the Proposed Operating Airspace (character aspects of particular air spaces – regardless of class)',
        'firstctrl12':'Describe location of the control station',
        'firstctrl13':'Comments',
        'secondctrl1':'Describes the intended mission of the UAS (surveillance, agricultural applicator, cargo delivery, etc.)',
        'secondctrl2':'Comments',
        'thirdctrl1':'Identifies Airspace Considerations (peculiarities & congestion of particular airspace, special use, etc.)',
        'thirdctrl2':'Gives Launch & Recovery Details/ Location(s)',
        'thirdctrl3':' Identifies and describes the vehicle’s proximity to people, infrastructure and surface vehicles.',
        'thirdctrl4':' Identifies and describes the vehicle’s proximity to other NAS users',
        'thirdctrl5':'Identifies whether they want to Fly Into Known Icing (FIKI)',
        'thirdctrl6':'Identifies the meteorological conditions they want to operate in (Visual/Instrument conditions)',
        'thirdctrl7':'Identifies the flight rules they want to operate in (Visual / Instrument Flight Rules)',
        'thirdctrl8':'Describes whether their geographic and airspace boundaries are physically contiguous',
        'thirdctrl9':'Identifies the Automation Level (occasional autopilot, 100% autonomous, manual control, etc.)',
        'thirdctrl10':'Identifies minimum crew and support personnel',
        'thirdctrl11':'Identifies the role(s) of the crew and support personnel',
        'thirdctrl12':'Identifies whether they will fly over people not involved in the operation',
        'thirdctrl13':'Identifies any requests for airspace be blocked-off for their exclusive use.',
        'thirdctrl14':'Identifies their operator/vehicle ratio (1:1, etc.)',
        'thirdctrl15':'Identifies day and/or night operations',
        'thirdctrl16':'Plans for safety of Operator(s) and Observer(s)',
        'thirdctrl17':'Describes the training level of each team member',
        'thirdctrl18':'Comments',
        'fourtctrl1': 'Describes Community Outreach Plans (Flying / Non-Flying Public, municipalities, airports, etc.)',
        'fourtctrl2': 'Describes when/ if flight plans will be filed with Air Traffic Control (VFR/IFR)',
        'fourtctrl3': 'Identifies Liaisons with Air Traffic Control',
        'fourtctrl4': 'Identifies MISHAP Reporting Procedures',
        'fourtctrl5': 'Identifies when NOTAMs will be posted',
        'fourtctrl6': 'Comments',
        'fivectrl1': 'Describes Communication Between The Operator, Observer and Crew Members (visual, radio, etc.)',
        'fivectrl2': 'Describes the Electronic Security of the Control Link',
        'fivectrl3': 'Describes the Physical Security of the operator and control station',
        'fivectrl4': 'Describes real time situational awareness features',
        'fivectrl5': 'Describes the number of operators, and hand-off between control stations (direct/“daisy chain”, etc.)',
        'fivectrl6': 'Describes Lost Link Procedures or loss of Positive Control',
        'fivectrl7': 'Describes Communication Expectations w/ATC',
        'fivectrl8': 'Describes Emergency Procedures'
    }

engine = create_engine(SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()


@appbuilder.app.route('/api/forms', methods=['POST'])
@cross_origin()
def get_json():

    data = request.get_json()
    #Json to dictionary
    data_dict = json.loads(json.dumps(data))
    #New Object
    new_instance = Form()

   #firstForm (new_instance.firstctrl1 = data_dict.get("firstForm", {}).get("firstCtrl1", "default"))

    for i in range(1, 14):
        field_name = f"firstCtrl{i}"
        setattr(new_instance, f"firstctrl{i}", data_dict.get("firstForm", {}).get(field_name, ""))

    #SecondForm
    for e in range(1, 3):
        field_name = f"secondCtrl{e}"
        setattr(new_instance, f"secondctrl{e}", data_dict.get("secondForm", {}).get(field_name, ""))

    #thirdForm
    for a in range(1, 19):
        field_name = f"thirdCtrl{a}"
        setattr(new_instance, f"thirdctrl{a}", data_dict.get("thirdForm", {}).get(field_name, ""))

    #fourtForm
    for o in range(1, 8):
        field_name = f"fourtCtrl{o}"
        setattr(new_instance, f"fourtctrl{o}", data_dict.get("fourtForm", {}).get(field_name, ""))

    #fiveForm
    for u in range(1, 10):
        field_name = f"fiveCtrl{u}"
        setattr(new_instance, f"fivectrl{u}", data_dict.get("fiveForm", {}).get(field_name, ""))
    
    new_instance.created_at = func.now()
   
    session.add(new_instance)
    session.commit()
    session.close()

    response_data = {'message': 'JSON recibido correctamente',
                     'data': data}
    
    export_word(data)
    
    return jsonify(response_data)




def export_word(data):
    #get last id
    last_id = get_last_id()
    #load word template
    doc = DocxTemplate(os.path.join(basedir,'app','templates', 'static','doc','form.docx'))
    # Data (Json) to dictirionary
    data_dict = json.loads(json.dumps(data))
    # dict to word variables
    doc.render(data_dict)
    #Save doc
    doc.save(os.path.join(basedir,'app','templates', 'static','doc',"docs", f'smeac_form_{last_id}.docx'))
    #download doc
    
@appbuilder.app.route('/download')
def download_file():
    #get last id
    last = get_last_id()
    return send_from_directory('templates/static/doc/docs', f'smeac_form_{last}.docx')


def get_last_id():
    last = session.query(Form).order_by(Form.id.desc()).first()
    if last:
        session.close()
        return last.id
    else:
        session.close()
        return 1
    

@appbuilder.app.route('/')
def index():
    return render_template('frontend/index.html')

@appbuilder.app.route('/<path:path>')
def send_static(path):
    #print(f'templates/frontend/{path}')
    return send_from_directory('templates/frontend/', path)



appbuilder.add_view(
    FormView,
    "Form",
    icon="fa-folder-open-o",
    category="Forms",
    category_icon='fa-envelope'
)


"""
    Application wide 404 error handler
"""

@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return (
        render_template(
            "404.html", base_template=appbuilder.base_template, appbuilder=appbuilder
        ),
        404,
    )

db.create_all()
