import { Component } from '@angular/core';
import { RestService } from './Services/rest.service';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Angular 11 Multiple Images Upload with Preview';
  constructor(private rs : RestService){}

  headers = ["day","temperature", "windspeed",  "event"]


}
