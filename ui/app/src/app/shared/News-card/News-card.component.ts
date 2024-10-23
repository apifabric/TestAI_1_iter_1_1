import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './News-card.component.html',
  styleUrls: ['./News-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.News-card]': 'true'
  }
})

export class NewsCardComponent {


}