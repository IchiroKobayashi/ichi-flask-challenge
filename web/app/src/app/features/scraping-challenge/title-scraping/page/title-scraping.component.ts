import { Component, OnInit, OnDestroy, ViewEncapsulation } from '@angular/core';
import { ActivatedRoute, Router } from "@angular/router";
import { BehaviorSubject, Observable, Subject, Subscription } from "rxjs";
import { FormBuilder, FormsModule, FormControl } from '@angular/forms';
import { TitleScrapingService } from '../service/title-scraping.service';
import { TweetScrapingEntity } from '../model/title-scraping.model';
import { TEXT } from '../../../../../resources/texts/features/scraping-challenge/title-scraping/text';

@Component({
  selector: 'app-title-scraping',
  templateUrl: './title-scraping.component.html',
  styleUrls: ['./title-scraping.component.less'],
  encapsulation: ViewEncapsulation.None
})
export class TitleScrapingComponent implements OnInit, OnDestroy {

  // Constructor DI
  constructor(
    private service: TitleScrapingService,
    private route: ActivatedRoute,// To receive parameters
    private router: Router,// For Transition
    private formBuilder: FormBuilder,
  ) { }

  // Property Definition
  destroyed$ = new Subject();
  private subscriptions: Array<Subscription> = [];
  tweets: Array<string>;
  limit: number = 10;
  isTweet: boolean = false;
  twitterUserName: string;
  texts: { [key:string]: string};
  pageReady: boolean = false;

  ngOnDestroy(): void {
    this.destroyed$.next();
    this.destroyed$.complete();
    this.subscriptions.forEach(removeSubscription => removeSubscription.unsubscribe());
  }

  ngOnInit(): void {
    this.subscriptions.push(
      TEXT().subscribe(res =>{
        this.texts = res;
      })
    );
    this.tweets = [];
    this.pageReady = true;
  }

  getTweetsById(): void {
    this.tweets = [];
    this.isTweet = false;
    this.subscriptions.push(
      this.service.getTweetsById(this.twitterUserName, this.limit).subscribe(response => {
        if(response.tweets.length > 0) {
          this.isTweet = true;
        }
        this.tweets = response.tweets;
      })
    );
  }

  getHondaTweets(): void {
    this.tweets = [];
    this.isTweet = false;
    this.subscriptions.push(
      this.service.getHondaTweets(this.limit).subscribe(response => {
        if(response.tweets.length > 0) {
          this.isTweet = true;
        }
        this.tweets = response.tweets;
      })
    );
  }

}
