
import { Component, OnInit } from '@angular/core';
@Component({
  selector: 'app-succefull',
  templateUrl: './succefull.component.html',
  styleUrls: ['./succefull.component.scss']
})
export class SuccefullComponent implements OnInit {
  mostrarBotonDescarga = false;
  ngOnInit() {
    // Después de un cierto período de tiempo (en milisegundos), cambia el valor de la variable para mostrar el botón.
    setTimeout(() => {
      this.mostrarBotonDescarga = true;
    }, 1500); // 1500 milisegundos = 1.5 segundos
  }
}