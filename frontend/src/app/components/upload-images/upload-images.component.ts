import { Component, OnInit } from '@angular/core';
import { HttpEventType, HttpResponse, HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { FileUploadService } from 'src/app/services/file-upload.service';
@Component({
  selector: 'app-upload-images',
  templateUrl: './upload-images.component.html',
  styleUrls: ['./upload-images.component.css']
})
export class UploadImagesComponent implements OnInit {

  selectedFiles?: FileList;
  progressInfos: any[] = [];
  message: string[] = [];

  previews: string[] = [];
  imageInfos:Array<any> = [];
  pages :number = 0;
  //imageInfos?: Observable<any>;

  constructor(private uploadService: FileUploadService, private http : HttpClient) { }

  ngOnInit(): void {
    //this.imageInfos = []
    this.pages = 0

  }
weatherUrl : string = "http://127.0.0.1:5000/weatherReport";
  selectFiles(event: any): void {
    this.message = [];
    this.progressInfos = [];
    this.selectedFiles = event.target.value;

    this.previews = [];
    this.pages = 0
  }

  upload(text:any): void {

    var page = (<HTMLInputElement>document.getElementById("page")).value
    console.log(text)
 
     this.http.get(this.weatherUrl+"?query="+text+"&page="+page).subscribe
        (
          (response:any) => 
          {
            console.log(response.length)
            if (response.length > 0) {
              for (let i = 0; i < response.length; i++) {
                console.log(response[i]['_source']['local_url']);
                //this.imageInfos[i]['url'] = response[i]['_source']['local_url'];
                //this.imageInfos[i]['name'] = response[i]['_source']['image_id'];
                //this.imageInfos[i]['description'] = response[i]['_source']['alt'];
                this.imageInfos[i] = {'url':response[i]['_source']['local_url'], 'name':response[i]['_source']['image_id'], 'description':response[i]['_source']['alt']}
              }
              this.pages += 10
              console.log(this.imageInfos)
            }
            //this.weather = response[0]["data"];
          },
          (error:any) =>
          {
            console.log("No Data Found" + error);
          }

        );

    //this.progressInfos[idx] = { value: 0, fileName: file.name };

    /*if (file) {
      this.uploadService.upload(file).subscribe(
        (event: any) => {
          if (event.type === HttpEventType.UploadProgress) {
            //this.progressInfos[idx].value = Math.round(100 * event.loaded / event.total);
          } else if (event instanceof HttpResponse) {
            const msg = 'Uploaded the file successfully: ' + file.name;
            this.message.push(msg);
            this.imageInfos = this.uploadService.getFiles();
          }
        },
        (err: any) => {
          //this.progressInfos[idx].value = 0;
          const msg = 'Could not upload the file: ' + file.name;
          this.message.push(msg);
        });
    }*/
  }

  uploadFiles(): void {
    this.message = [];

    var test = document.getElementById('page') as HTMLElement
    console.log(test);

    console.log()

    if (this.selectedFiles) {
      this.upload(this.selectedFiles);
      for (let i = 0; i < this.selectedFiles.length; i++) {
        //this.upload(i, this.selectedFiles[i]);
      }
    }
  }
}
