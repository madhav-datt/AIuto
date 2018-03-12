# AIuto

**Aiuto.** *Help.*

The word is so powerful. When asking for help, we are often at our most vulnerable. We may be scared, lonely or embarrassed. It can be difficult to ask for help, but without aid from others, many people would struggle to survive.

**Aiuto.** *Help.*

It can be one of the most profound and intimate things humans can do for each-other. What seems like a small action for you could cause major improvements to someone else's quality of life.

**AIuto.** *Our project.*

Using artificial intelligence (AI), we can provide this help. We can optimise for certain issues that prevent refugees getting the aid they require (language barriers, distance and willingness to donate).

### Inspiration

Imagine you were a high school student in Syria when the war broke out. You were forced to leave behind everything and everyone you know, and get on a boat into the unknown. After spending weeks on Mediterranean waters, you reach someplace far from what you used to call home, where you don't have a place to live, can't find the job, and don't speak the language. People in these communities need immediate solutions. Being able to get access to simple, everyday things like water, clothes, and temporary shelter become a matter of survival. In this project, we use artificial intelligence technology to develop a very human centered solution to help people facing these immediate and acute crises situations.

### Our process and thinking

After some of the excellent talks we have attended over the last two days, the entire team felt empowered to make something that would make the world a better place.

Having been selected to take part in the Migrants and Refugees track based on our enthusiasm for making a real difference in this area, we started the hackathon by brainstorming. For hours and hours, new ideas flowed. Some were entirely unfeasible (for example, while AR/VR solutions are interesting, they are a technology that is almost entirely impossible to access in the circumstances a refugee faces.)

One extremely long foundations session later, and we had narrowed our ideas down. The most important thing in any project of this nature is obviously the reach/accessibility of the solution produced. After some research, we found that around 70% of refugees own a mobile phone (though only approximately 30% have internet-enabled mobile phones). For this reason, we decided to target something **all** mobile phones are capable of - SMS.

While it may not be the newest or shiniest of technologies, the fact SMS is a long established capability means a much wider support for it in less developed countries, and even the cheapest of mobile phones will be capable of it!

Furthermore, privacy and safety is becoming more and more of a concern for online interaction. It is for this reason (among others) that all personal data is never directly distributed to the either user until they agree to exchange this information. This prevents harassment or misuse of both parties details.

### What it does

The system acts as a helpline for migrants and refugees, anonymising their call for education/companionship/basic immediate human needs. This protects the user from further harm by malicious individuals.

They can text our special AIuto phone number, and after a brief chatbot interaction where their need and location is identified, we search Twitter (one of the most open and simple to use social media platforms) to find tweets from the local area mentioning migrants and refugees. Depending on the required aid (for example human companionship and conversation) we may also filter based on language.

*The need for human interaction cannot be underestimated, and while offering food/drink and services, sometimes humans just need to be listened to by other humans.*

These tweets are then run through a sentiment analysis engine, so we can intelligently gauge how our potential aid providers feel towards M&Rs. A handful of the most positive local Twitter users are selected, and directly tweeted a reference number. This facilitates communication between the two parties while maintaining anonymity - a growing concern in society today.

From this point, our SMS messaging service provides on-the-fly translation between both the refugee and the supporter with absolutely no need for the internet. A relationship can build as trust between the chat participants builds. A place to convene can be organised, and the required items can be provided to those in need.

This relationship can be maintained longer term in this respect, because it is entirely up to the participants to continue interacting.

### How we built it

Twilio was used to allow a data-free SMS service to interact with the Internet. From there, all of the heavy lifting is done using Python - more specifically Tweepy to help integrate with Twitter, and the Microsoft Cognitive Services API (writing our own was considered, though we decided this was uneconomical use of our time).

### Challenges we ran into

While M&Rs experience interacting with the system is entirely data-free, to actually develop the application we heavily relied on access to the Internet. Connection was occasionally dropped, which made debugging (and overall development) slightly more long-winded than expected. However, we used this 'dead time' more appropriately with other offline activities.

Getting the Twilio integrations working was also challenging. SMS in a foreign country turned out to open many questions (how much am I getting charged for this text? What are the limitations of the free account?).

Jet-lag has also been another major factor for some team members. Travelling overseas to new countries is exciting, but undeniably a tiring experience.

### Accomplishments that we are proud of

Contributing to society and being part of such a rich and cultural event is an amazing opportunity and something we are all proud of. By even being selected we are all humbled and thankful.

More project-specifically, the collaboration in our team has been fantastic from the first few moments to the very end. Only a few days ago, we were all complete strangers, but now we are so much more.

The delegation and separation of roles has led to a far more structured and consistent development methodology, while the trust we all have in each-other's abilities allows us to not worry about parts of the system we are not responsible for.

Furthermore, the use of a wide range of technologies (a handful of which most of the team have never used before) means that not only has the event been an educational one culturally, but also technologically.

Finally, the creation of an entire end-to-end system which behaves consistently and as expected, paired with a beautiful website and fully thought plans for sustaining this endeavour as long as possible means this is without a doubt the hackathon we are all most proud of. None of us could have dreamed of producing a more polished product in such a small time.

### What we learned

There was a great deal of education in this trip. While we each have broadened our horizons technically (pair programming together has exposed us to different ways of work, and challenged us to think in new and exciting ways), the largest part of education is undoubtedly learning more about the issues M&Rs face on a daily basis, and finding out about feasible solutions to very real and catastrophic problems.

### What next for AIuto?

So much more. While our current solution is scaleable, we can optimise. Partnerships with willing companies would allow us to purchase subscriptions to faster or more powerful toolsets.

Widening the platform to analyse not only Twitter, but a variety of other metrics is another step that would improve the quality of results.

Improving the awareness of this solution. If people do not use the platform, it is of no use to anyone. We should market this, hand out leaflets and pamphlets in a variety of languages and encourage users to spread this by word of mouth.

Partnerships using local businesses with excess food that may be donated, to not only help refugees but also reduce waste.

The possibilities are endless. If this entire system and roadmap can be created to a high quality in only 36 hours, imagine what could be produced in even more time.

#### This README can be found in the following languages:
* [Arabic](https://pastebin.com/ZRPFcgXL)
* [French](https://pastebin.com/4Rs7T2HJ)
* [Italian](https://pastebin.com/aQwJDSas)

### Made with :heart: at the Vatican, by [Madhav Datt](https://github.com/madhav-datt), [Sam Warner](https://github.com/sjwarner), [Ge Gao](https://github.com/gg0027), [Ryan Rose](https://www.linkedin.com/in/hiromurose/), and [Ibrahim Malik]()
