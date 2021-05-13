import { Observable } from "rxjs";
import { Injectable} from "@angular/core";
import { HttpClient} from "@angular/common/http";
import { TweetScrapingEntity } from '../model/title-scraping.model';
import { ScrapingChallengeConst } from '../../constant/scraping-challenge-const';

@Injectable()
export class TitleScrapingService {

  constructor(
    private http: HttpClient
  ) {
  }

  getTweets(twitterUserName: string): Observable<TweetScrapingEntity>{
    return this.http.get<TweetScrapingEntity>(
      ScrapingChallengeConst.API_URL + 'scrape',
      {
        params:{
          twitterUserName: twitterUserName
        }
      }
    )
  }

}
