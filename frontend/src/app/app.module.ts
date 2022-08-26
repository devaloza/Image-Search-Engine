import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';

import { AppComponent } from './app.component';
import { UploadImagesComponent } from './components/upload-images/upload-images.component';
import { RestService } from './Services/rest.service';

@NgModule({
  declarations: [
    AppComponent,
    UploadImagesComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule
  ],
  providers: [RestService],
  bootstrap: [AppComponent]
})
export class AppModule { }
