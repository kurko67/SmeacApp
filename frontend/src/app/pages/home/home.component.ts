import { Component, OnInit  } from '@angular/core';
import { Router } from '@angular/router';
import { Validators, FormBuilder, NgForm, FormGroup } from '@angular/forms';
import { STEPPER_GLOBAL_OPTIONS } from '@angular/cdk/stepper';
import { PaginatorService } from './paginator.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss'],
  providers: [
    {
      provide: STEPPER_GLOBAL_OPTIONS,
      useValue: { showError: true },
    },
  ],
})
export class HomeComponent implements OnInit{
  homeForm: MtecForm = new MtecForm();
  firstFormGroup!: FormGroup;
  secondFormGroup!: FormGroup;
  thirdFormGroup!: FormGroup;
  fourtFormGroup!: FormGroup;
  fiveFormGroup!: FormGroup;

  currentPage: number = 0;


  constructor(private _formBuilder: FormBuilder, private paginatorService: PaginatorService, private router: Router ) {
    this.initForm();
  }

   ngOnInit(): void {
    
    
  }

  goToNextPage(): void {
    if (this.validateCurrentPage()) {
      this.currentPage++;
    }
  }

  goToPreviousPage(): void {
    if (this.currentPage > 0) {
      this.currentPage--;
    }
  }

  validateCurrentPage(): boolean {
    // Realiza la validación según los campos del formulario actual
    switch (this.currentPage) {
      case 0:
        return this.validateFormGroup(this.firstFormGroup);
      case 1:
        return this.validateFormGroup(this.secondFormGroup);
      case 2:
        return this.validateFormGroup(this.thirdFormGroup);
      case 3:
        return this.validateFormGroup(this.fourtFormGroup);
      case 4:
        return this.validateFormGroup(this.fiveFormGroup);
      default:
        return true; // Si no hay validación específica para la página actual, permite avanzar
    }
  }

  
    // Función de validación genérica para un FormGroup
    validateFormGroup(formGroup: FormGroup): boolean {
      if (formGroup.valid) {
        return true;
      } else {
        // Muestra un mensaje de error o realiza alguna acción
        alert('Please complete all form fields before continuing.');
        return false;
      }
    }



  onSubmit(): void {


      if(this.validateCurrentPage()) {

        const dataFormJson = JSON.stringify(this.homeForm);
    
        // Enviar los datos al servidor Flask usando la función fetch
        fetch('/api/forms', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: dataFormJson,
        })
            .then(response => {
                if (response.ok) {
                    // La solicitud fue exitosa
                    return response.json();

                } else {
                    // Manejar errores aquí
                    throw new Error('Error en la solicitud HTTP');
                }
            })
            .then(data => {
                // Manejar la respuesta del servidor Flask, si es necesario
            })
            .catch(error => {
                // Manejar errores, si es necesario
                console.error(error);
            });
    
            console.log('Formulario datos : ', dataFormJson);
            this.router.navigate(['./../succefull']);
            

      } else{

        console.log('Please complete all form fields before continuing.');
        

      }

}


  initForm() {
    this.firstFormGroup = this._formBuilder.group({
      firstCtrl1: ['', Validators.required ],
      firstCtrl2: ['', Validators.required ],
      firstCtrl3: ['', Validators.required ],
      firstCtrl4: ['', Validators.required ],
      firstCtrl5: ['', Validators.required ],
      firstCtrl6: ['', Validators.required ],
      firstCtrl7: ['', Validators.required ],
      firstCtrl8: ['', Validators.required ],
      firstCtrl9: ['', Validators.required ],
      firstCtrl10:['', Validators.required],
      firstCtrl11: ['', Validators.required],
      firstCtrl12:['', Validators.required],
      firstCtrl13: ['', Validators.required],
    });
    this.secondFormGroup = this._formBuilder.group({
      secondCtrl1: ['', Validators.required],
      secondCtrl2: ['', Validators.required],
    });
    this.thirdFormGroup = this._formBuilder.group({
      thirdCtrl1: ['', Validators.required],
      thirdCtrl2: ['', Validators.required],
      thirdCtrl3: ['', Validators.required],
      thirdCtrl4: ['', Validators.required],
      thirdCtrl5: ['', Validators.required],
      thirdCtrl6: ['', Validators.required],
      thirdCtrl7: ['', Validators.required],
      thirdCtrl8: ['', Validators.required],
      thirdCtrl9: ['', Validators.required],
      thirdCtrl10: ['', Validators.required],
      thirdCtrl11: ['', Validators.required],
      thirdCtrl12: ['', Validators.required],
      thirdCtrl13: ['', Validators.required],
      thirdCtrl14: ['', Validators.required],
      thirdCtrl15: ['', Validators.required],
      thirdCtrl16: ['', Validators.required],
      thirdCtrl17: ['', Validators.required],
      thirdCtrl18: ['', Validators.required],
    });
    this.fourtFormGroup = this._formBuilder.group({
      fourtCtrl1: ['', Validators.required],
      fourtCtrl2: ['', Validators.required],
      fourtCtrl3: ['', Validators.required],
      fourtCtrl4: ['', Validators.required],
      fourtCtrl5: ['', Validators.required],
      fourtCtrl6: ['', Validators.required],
    });
    this.fiveFormGroup = this._formBuilder.group({
      fiveCtrl1: ['', Validators.required],
      fiveCtrl2: ['', Validators.required],
      fiveCtrl3: ['', Validators.required],
      fiveCtrl4: ['', Validators.required],
      fiveCtrl5: ['', Validators.required],
      fiveCtrl6: ['', Validators.required],
      fiveCtrl7: ['', Validators.required],
      fiveCtrl8: ['', Validators.required],
    });
  }
}

class MtecForm {
  firstForm = {
    firstCtrl1: '',
    firstCtrl2: '',
    firstCtrl3: '',
    firstCtrl4: '',
    firstCtrl5: '',
    firstCtrl6: '',
    firstCtrl7: '',
    firstCtrl8: '',
    firstCtrl9: '',
    firstCtrl10: '',
    firstCtrl11: '',
    firstCtrl12: '',
    firstCtrl13: '',
  };
  secondForm = {
    secondCtrl1: '',
    secondCtrl2: '',
  };
  thirdForm = {
    thirdCtrl1: '',
    thirdCtrl2: '',
    thirdCtrl3: '',
    thirdCtrl4: '',
    thirdCtrl5: '',
    thirdCtrl6: '',
    thirdCtrl7: '',
    thirdCtrl8: '',
    thirdCtrl9: '',
    thirdCtrl10: '',
    thirdCtrl11: '',
    thirdCtrl12: '',
    thirdCtrl13: '',
    thirdCtrl14: '',
    thirdCtrl15: '',
    thirdCtrl16: '',
    thirdCtrl17: '',
    thirdCtrl18: '',
  };
  fourtForm = {
    fourtCtrl1: '',
    fourtCtrl2: '',
    fourtCtrl3: '',
    fourtCtrl4: '',
    fourtCtrl5: '',
    fourtCtrl6: '',
  };
  fiveForm = {
    fiveCtrl1: '',
    fiveCtrl2: '',
    fiveCtrl3: '',
    fiveCtrl4: '',
    fiveCtrl5: '',
    fiveCtrl6: '',
    fiveCtrl7: '',
    fiveCtrl8: '',
  };
}
