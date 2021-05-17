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

  getTweetsById(twitterUserName: string, limit?: number): Observable<TweetScrapingEntity>{
    return this.http.get<TweetScrapingEntity>(
      ScrapingChallengeConst.API_URL + 'getTweetsById',
      {
        params:{
          twitterUserName: twitterUserName,
          limit: limit + ''
        }
      }
    )
  }

  getHondaTweets(limit?:number): Observable<TweetScrapingEntity>{
    return this.http.get<TweetScrapingEntity>(
      ScrapingChallengeConst.API_URL + 'getHondaTweets',
      {
        params:{
          limit: limit + ''
        }
      }
    )
  }

}
