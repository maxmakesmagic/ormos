---
id: kgjb9ym4
kind: article
lang: en
path: /en/articles/feature/2017/12-01-the-stack-and-its-tricks
title: The Stack and Its Tricks
published: '2017-12-01'
column_slug: feature
column: Feature
authors:
- slug: gavin-verhey-375b82f9
  name: Gavin Verhey
detected_lang: en
metadata_evidence:
  title:
    page_key: magic.wizards.com/en/news/feature/stack-and-its-tricks-2017-11-30
    lang_detected: en
    capture_id: 192189
    url: https://magic.wizards.com/en/news/feature/stack-and-its-tricks-2017-11-30
    captured_at: '2024-05-18 02:42:59+00'
    rule: jsonld.headline
  published:
    page_key: magic.wizards.com/en/news/feature/stack-and-its-tricks-2017-11-30
    lang_detected: en
    capture_id: 192189
    url: https://magic.wizards.com/en/news/feature/stack-and-its-tricks-2017-11-30
    captured_at: '2024-05-18 02:42:59+00'
    rule: jsonld.date_published
  authors:
    page_key: magic.wizards.com/en/news/feature/stack-and-its-tricks-2017-11-30
    lang_detected: en
    capture_id: 192189
    url: https://magic.wizards.com/en/news/feature/stack-and-its-tricks-2017-11-30
    captured_at: '2024-05-18 02:42:59+00'
    rule: jsonld.author
  column:
    page_key: magic.wizards.com/en/news/feature/stack-and-its-tricks-2017-11-30
    lang_detected: en
    capture_id: 192189
    url: https://magic.wizards.com/en/news/feature/stack-and-its-tricks-2017-11-30
    captured_at: '2024-05-18 02:42:59+00'
    rule: url.article_section
    registry_match: registry.explicit
sources:
- document_id: kgjb9ym4
  url: https://magic.wizards.com/en/news/feature/stack-and-its-tricks-2017-11-30
  page_key: magic.wizards.com/en/news/feature/stack-and-its-tricks-2017-11-30
  lang: en
  template: contentful
  captured_at: '2024-05-18 02:42:59+00'
  capture_id: 192189
  wayback_url: https://web.archive.org/web/20240518024259id_/https://magic.wizards.com/en/news/feature/stack-and-its-tricks-2017-11-30
- document_id: kgjb9ym4
  url: https://magic.wizards.com/en/articles/archive/beyond-basics/stack-and-its-tricks-2017-11-30
  page_key: magic.wizards.com/en/articles/archive/beyond-basics/stack-and-its-tricks-2017-11-30
  lang: en
  template: drupal
  captured_at: '2022-08-10 21:03:44+00'
  capture_id: 229461
  wayback_url: https://web.archive.org/web/20220810210344id_/https://magic.wizards.com/en/articles/archive/beyond-basics/stack-and-its-tricks-2017-11-30
source_selection: The catalog's primary source rendered.
archive_source:
  document_id: kgjb9ym4
  capture_id: 192189
  url: https://magic.wizards.com/en/news/feature/stack-and-its-tricks-2017-11-30
  wayback_url: https://web.archive.org/web/20240518024259id_/https://magic.wizards.com/en/news/feature/stack-and-its-tricks-2017-11-30
  captured_at: '2024-05-18 02:42:59+00'
  template: contentful
  sha256: d622c9bdccf236a01be959f49e1c4aba0d4d8178a8e37c643657fb1ca953c4b0
render_recovery:
- code: unsupported_link
  element: a
  target: mailto:BeyondBasicsMagic@Gmail.com
  reason: The archived link opens an email client. The preview kept its text.
  labels:
  - BeyondBasicsMagic@Gmail.com
  occurrences: 1
---
The stack.

Those are two words that are sometimes whispered in hushed tones across *Magic* circles. The zone not to teach or talk about. To try and keep invisible.

And while it's true that we don't try to teach the stack to new players, since it's an extra bit of confusing information to keep track of as you're trying to learn the already intricate and potentially overwhelming game of *Magic*, it's an important piece of the game.

In a way, sitting down and explaining the stack is kind of like the birds and the bees talk of *Magic*.

My friend Dino started playing *Magic* recently. (I'm thanking the Dino-saurs for this one.) He asked me for some good resources on how the stack works, and for how to best take advantage of it. And after combing through various DailyMTG articles and cross-linking them for a while, I noticed there hadn't been a lot said about the topic all in one place recently.

So let's change that.

What is the stack, how does it work, and what are some tricks you can pull off with it?

It's time to take a look!

# The Stack: An Introduction

In short, the stack is the limbo that *Magic* spells and abilities go to between being activated or cast and actually happening.

In this liminal space, you know something is going to happen, it just hasn't happened yet.

It basically works like this:

I play a spell. Any spell—creature, instant, artifact, whatever. It goes onto the stack.

The player whose turn it is (in this case, me) gets a chance to respond. This chance to respond is called "priority." Then my opponent gets a chance to respond. If neither of us do, then the spell just happens. Easy.

But let's say that my opponent responds with a spell. Well, then we both have an opportunity to do something again.

As soon as we both elect to do nothing, my opponent's spell resolves.

Now, my original spell is still on the stack. Once we both pass priority, it will resolve.

Notice something there? The thing that was cast second happened before the first one. The stack is a last-in-first-out system.

Let's try a real example to help visualize this.

I cast [Walking Corpse](https://web.archive.org/web/20171201000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Walking+Corpse).

I gain priority, and elect to not respond to my own spell. I pass priority. If my opponent also elects to do nothing, [Walking Corpse](https://web.archive.org/web/20171201000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Walking+Corpse) will enter the battlefield.

However, in this case, my opponent casts [Anticipate](https://web.archive.org/web/20171201000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Anticipate) in response.

![](https://media.wizards.com/2017/images/daily/BB20171130_Stack01.png)

I pass priority. My opponent passes priority. [Anticipate](https://web.archive.org/web/20171201000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Anticipate) happens.

Then I get priority back. [Anticipate](https://web.archive.org/web/20171201000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Anticipate) is in the graveyard, but [Walking Corpse](https://web.archive.org/web/20171201000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Walking+Corpse) is still on the stack. I pass priority. If my opponent passes priority, my [Walking Corpse](https://web.archive.org/web/20171201000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Walking+Corpse) will resolve. They do, and so [Walking Corpse](https://web.archive.org/web/20171201000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Walking+Corpse) enters the battlefield.

But note that if they had, say, a [Cancel](https://web.archive.org/web/20171201000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Cancel) (perhaps one they took off [Anticipate](https://web.archive.org/web/20171201000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Anticipate)!), they could have used it to counter that Corpse.

Now, this is a lot of technical details. In most games of *Magic*, this is totally obfuscated and correctly replaced by just saying "[Walking Corpse](https://web.archive.org/web/20171201000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Walking+Corpse), go." But there are times when the stack becomes important.

Let's talk practical applications.

# The Bolt and the Bear

There's a tale as old as time: the Bolt and the Bear.

I have a [Runeclaw Bear](https://web.archive.org/web/20171201000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Runeclaw+Bear). I attack.

I have [Titanic Growth](https://web.archive.org/web/20171201000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Titanic+Growth) in my hand, so I cast it! Take 4 more, my enemy!

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Titanic+Growth)](https://web.archive.org/web/20171201000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Titanic+Growth)

I gain priority with [Titanic Growth](https://web.archive.org/web/20171201000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Titanic+Growth). I pass priority. But my opponent, grinning, takes this chance to tap a Mountain and cast [Lightning Bolt](https://web.archive.org/web/20171201000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lightning+Bolt) on the poor Bear!

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Lightning+Bolt)](https://web.archive.org/web/20171201000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lightning+Bolt)

I gain priority again. I pass. My opponent also passes. Bolt resolves and . . . the Bear dies. [Titanic Growth](https://web.archive.org/web/20171201000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Titanic+Growth) is still on the stack, but it won't resolve. The card "fizzles"—it's countered by the game rules because it no longer has a valid target. Sad times.

Now let's flip the script.

The situation is the same: I'm attacking with the Bear. Except this time, I don't cast [Titanic Growth](https://web.archive.org/web/20171201000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Titanic+Growth).

My opponent takes the opportunity to cast [Lightning Bolt](https://web.archive.org/web/20171201000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lightning+Bolt) before damage happens. I get priority back—and I cast [Titanic Growth](https://web.archive.org/web/20171201000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Titanic+Growth)!

My Bear becomes a 6/6, [Lightning Bolt](https://web.archive.org/web/20171201000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lightning+Bolt) doesn't kill the Bear, and my opponent takes 6 damage.

That is a pretty tremendous difference!

![](https://media.wizards.com/2017/images/daily/BB20171130_Bear.png)

Sometimes in situations like this, neither player will cast either spell for fear of the unfavorable situation happening. Remember, the last player to do something generally has the power.

Also, let this be a lesson on why it's dangerous to deal damage to attacking creatures when your opponent is representing combat tricks. (But for more on that, go read "[The Instances for Instants](/en/articles/feature/2017/06-08-the-instances-for-instants).")

# What Uses the Stack?

Here's a pretty common question: Which kinds of cards and abilities use the stack?

Pretty much any spell you cast, non-mana activated ability you use, or triggered ability you play is going to use the stack in exactly the same way as described above. Whether you're casting [Walking Corpse](https://web.archive.org/web/20171201000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Walking+Corpse), activating [Captivating Crew](https://web.archive.org/web/20171201000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Captivating+Crew), or triggering [God-Pharaoh's Gift](https://web.archive.org/web/20171201000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=God-Pharaoh%27s+Gift), they all use the stack.

![](https://media.wizards.com/2017/images/daily/BB20171130_Triggers.png)

For reference, an activated ability uses the template COST: Effect. Look for the colon. A triggered ability generally starts with "At," "When," or "Whenever."

It is also important to note that once an ability is on the stack, it will happen. If I activate my [Prodigal Pyromancer](https://web.archive.org/web/20171201000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Prodigal+Pyromancer) and you [Lightning Bolt](https://web.archive.org/web/20171201000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lightning+Bolt) it in response, the ability is still going to deal 1 damage even though the Pyromancer is gone.

So, what doesn't use the stack?

Well, for one, static abilities don't use the stack. [Platinum Angel](https://web.archive.org/web/20171201000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Platinum+Angel) doesn't keep triggering over and over; its effect is just always true while it's on the battlefield. (Initially casting [Platinum Angel](https://web.archive.org/web/20171201000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Platinum+Angel) will still use the stack, though.)

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Platinum+Angel)](https://web.archive.org/web/20171201000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Platinum+Angel)

Playing your land for the turn doesn't use the stack. You can just play it and nobody can respond.

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Unclaimed+Territory)](https://web.archive.org/web/20171201000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Unclaimed+Territory)

Mana abilities don't use the stack. A mana ability is an activated ability that adds mana to your mana pool. (There are rare exceptions to this, but let's ignore them for now.) So, for example, tapping lands or [Llanowar Elves](https://web.archive.org/web/20171201000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Llanowar+Elves) for mana can't be responded to and doesn't use the stack.

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Llanowar+Elves)](https://web.archive.org/web/20171201000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Llanowar+Elves)

Costs don't use the stack. If I cast [Fling](https://web.archive.org/web/20171201000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fling), you can't destroy the creature I want to sacrifice before I sacrifice it—that just happens.

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Fling)](https://web.archive.org/web/20171201000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Fling)

"As" abilities generally do not use the stack. For example, with a [Clone](https://web.archive.org/web/20171201000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Clone), once it resolves you can't see what creature it is copying and then decide to kill the creature.

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Clone)](https://web.archive.org/web/20171201000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Clone)

Those are some of the big ones I commonly see. There are others (yes, person over there who has been mouthing "morph" to me for the past three minutes, I see you), but for most games that's everything you need to know about what does and doesn't use the stack.

# Stack Tricks

Okay. So now that we've gone over how the stack actually works, what are some ways you can use the stack to your advantage?

There are plenty in *Magic*, but here are four worth mentioning. Fair warning that some of these get pretty technical, so if you're just learning the stack for the first time, don't feel bad if anything here is tricky to follow.

Advanced plays ahead!

1.  **Providing Unusual Windows to Respond**

Because you have this opportunity between things occurring, sometimes it's right to try and sneak a spell there in that gap of time.

A common example is against card-draw spells.

Your opponent casts [Divination](https://web.archive.org/web/20171201000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Divination) to draw two cards. Perhaps in response you cast a [Lightning Bolt](https://web.archive.org/web/20171201000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lightning+Bolt) on their creature, to take care of it in case they draw a [Titanic Growth](https://web.archive.org/web/20171201000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Titanic+Growth) or a counterspell. They're down mana, but haven't yet reaped the rewards. That's usually a pretty good time to make your move.

Not weird enough for you? Okay, here's one of my favorites.

The always-popular fetch lands (such as [Flooded Strand](https://web.archive.org/web/20171201000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Flooded+Strand)) have activated abilities, not mana abilities. That gives you a tiny window between when your opponent sacrifices the land and when they cast the spell they need the mana for.

It's a very narrow window . . . and also a clever time to cast something like [Vendilion Clique](https://web.archive.org/web/20171201000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Vendilion+Clique) to take away the card they were about to cast!

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Vendilion+Clique)](https://web.archive.org/web/20171201000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Vendilion+Clique)

 

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Flooded+Strand)](https://web.archive.org/web/20171201000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Flooded+Strand)

Always be looking for these tiny opportunities to respond. A lot of times it won't matter, but the one time in a hundred that it does, it can make a huge difference.

1.  **Holding Priority**

Throughout this article, I've mentioned time and time again that after you cast a spell or activate an ability on your turn, you get priority first, then your opponent does. Now, this very rarely matters. You seldom want to respond to yourself . . .

. . . But then again, there are a few times where you absolutely do.

A simple example would be something like [Reverberate](https://web.archive.org/web/20171201000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Reverberate): you want to hold priority so you can copy a spell you just cast.

A slightly more complex—but still common—event you see in Legacy is casting [Infernal Tutor](https://web.archive.org/web/20171201000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Infernal+Tutor), and then discarding your hand to [Lion's Eye Diamond](https://web.archive.org/web/20171201000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Lion%27s+Eye+Diamond) in response so you can go find any card.

A more extreme oldie but goodie in this space is fighting split second cards. (Did you think we were going to get through a whole article on the stack without a single split second example?)

Let's say you cast [Sacred Mesa](https://web.archive.org/web/20171201000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sacred+Mesa) and have six mana left. But you're worried your opponent might have a card that you can't respond to because of its split second ability: [Krosan Grip](https://web.archive.org/web/20171201000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Krosan+Grip).

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Sacred+Mesa)](https://web.archive.org/web/20171201000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sacred+Mesa)

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Krosan+Grip)](https://web.archive.org/web/20171201000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Krosan+Grip)

Well, you can activate the Mesa's ability in response to itself before your opponent ever gets the chance to respond! You're then guaranteed three Pegasus tokens even if they do have the Grip.

And speaking of responding to yourself . . .

1.  **Stacking Spells and Abilities**

Whatever was put on the stack most recently happens first. Sure.

Well then, you can get some pretty wacky results to happen if you time things right.

Let's say your opponent is at 6 life, and you have [Imminent Doom](https://web.archive.org/web/20171201000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Imminent+Doom) on the battlefield and two [Shock](https://web.archive.org/web/20171201000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Shock)s in your hand.

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Imminent+Doom)](https://web.archive.org/web/20171201000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Imminent+Doom)

You're just short of lethal damage, right?

Well, you actually can win from here!

If you cast the first [Shock](https://web.archive.org/web/20171201000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Shock), then respond with the second [Shock](https://web.archive.org/web/20171201000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Shock) before [Imminent Doom](https://web.archive.org/web/20171201000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Imminent+Doom)'s first trigger resolves, it will trigger twice! Your opponent will take 6! (And you'll have a three-counter [Imminent Doom](https://web.archive.org/web/20171201000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Imminent+Doom) to boot!)

Let's try another.

Here's one of my favorite mind-benders. How can you get to draw a card with [Sensei's Divining Top](https://web.archive.org/web/20171201000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Sensei%27s+Divining+Top), but not have the Top be the top card of your library?

Can you figure it out?

Here's what you do: Activate the ability to rearrange your top three cards, then in response tap the Top to draw a card. First you put the Top on top of your library, then you rearrange your top three cards. Go ahead and put that Top a little deeper down, why don't you?

You can do some similarly wild things with spells—especially if you find ways to give them flash. I'll give you an example.

There was a goofy combo deck that got to play two spells at the same time by way of the card [Spellweaver Helix](https://web.archive.org/web/20171201000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Spellweaver+Helix).

The two of choice? [Worldfire](https://web.archive.org/web/20171201000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Worldfire) and any spell that dealt damage.

You'd put the [Worldfire](https://web.archive.org/web/20171201000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Worldfire) on top of the burn spell and have that resolve first, and then the burn spell would still be hanging out on the stack ready to finish the game.

What ways can you think of to combine spells at odd times like this?

1.  **Counter Wars**

Knowing how to navigate a counterspell fight can be very important. A lot of cards are flying around on the stack—and you need to make sure the spell you don't want to resolve doesn't.

Targeting the right spell can be important, especially if your counterspell does more than just counter a spell.

One of my favorite example cards in this space is [Remand](https://web.archive.org/web/20171201000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Remand).

[![](https://gatherer.wizards.com/Handlers/Image.ashx?type=card&name=Remand)](https://web.archive.org/web/20171201000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Remand)

There's so much you can do with this card. Let's say you cast a spell. Your opponent tries to counter it. Well, instead of Remanding their counterspell, you [Remand](https://web.archive.org/web/20171201000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Remand) your own spell! Your spell comes back safely, and their counterspell does nothing.

Or let's go a level deeper.

Let's say your opponent casts a spell. You try and counter it. They counter your counter. Well, in this case, I'd consider just Remanding my original counterspell and using it again!

Whether using [Remand](https://web.archive.org/web/20171201000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Remand), [Summary Dismissal](https://web.archive.org/web/20171201000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Summary+Dismissal), [Memory Lapse](https://web.archive.org/web/20171201000000/https://gatherer.wizards.com/Pages/Card/Details.aspx?name=Memory+Lapse), or some other counterspell, be mindful of opportunities here.

# Stacking Things in Your Favor

Careful finesse is required to take full advantage of the stack, but once you understand how it works, you have the tools you need to swing these situations in your favor.

Hopefully you found this useful! I'd love to hear what you thought. Did you feel like this article was missing something? What are some of your favorite stack tricks? Tell me by sending a [tweet](http://www.twitter.com/gavinverhey), messaging me on [my Tumblr](http://www.gavinverhey.tumblr.com/), or emailing me at BeyondBasicsMagic@Gmail.com.

Talk with you again soon!

Gavin  
[@GavinVerhey](http://www.twitter.com/gavinverhey)  
[GavInsight](http://www.gavinverhey.tumblr.com/)