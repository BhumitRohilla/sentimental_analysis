const fs = require('fs');
const data = require('./combined.json');
const path = require('path');

const parsedData = [];

data.forEach((element) => {
    const data = {};
    const result = element.content?.itemContent?.tweet_results?.result?.legacy
    if (result) {
        data['tweetId'] = element.content.itemContent.tweet_results.result.rest_id;
        data['Message'] = result.full_text;
        data['userProfile'] = element.content.itemContent.tweet_results.result.core.user_results.result.legacy.profile_banner_url;
        data['userName'] = element.content.itemContent.tweet_results.result.core.user_results.result.legacy.name;
        data['userHandle'] = `${element.content.itemContent.tweet_results.result.core.user_results.result.legacy.screen_name}`;
        data['location'] = element.content.itemContent.tweet_results.result.core.user_results.result.legacy.location;
        data['date'] = result.created_at;
        data['hashtags'] = result.entities.hashtags;
        data['symbols'] = result.entities.user_mentions.map((userMention) => `${userMention.screen_name}`);
        data['lang'] = result.lang;
        data['favoriteCount'] =result.favorite_count;
        data['reply'] =result.reply_count;
        data['quote'] = result.quote_count;
        data['retweet'] = result.retweet_count;
        data['view'] = element.content.itemContent.tweet_results.result.views.count

        parsedData.push(data);
    }
})

console.log(parsedData.length);

fs.writeFileSync(path.join(__dirname, 'finalData.json'), JSON.stringify(parsedData));
