# GetXplain.AI — Extended Campaign Ideas + Exclusive Offer System

## Updated Rules

- Max **5 push/day** per user
- Max **2 emails/day** per user
- **Exception:** Exclusive Offer emails bypass the 2 email/day cap (tagged as transactional/exclusive)
- Working hours: 9am–9pm Cairo (Africa/Cairo)
- Exit on goal hit

---

## S0. THE EXCLUSIVE 24H OFFER (Priority Sales Campaign)

### Trigger Conditions (ALL must be true)

| # | Condition | Attribute | Check |
|---|-----------|-----------|-------|
| 1 | 5-Day Streak | `current_streak_days` | >= 5 |
| 2 | Finished 3 Library Lessons | `lessons_completed_count` | >= 3 |
| 3 | Created or Joined Squad 2x | `squads_joined_count + squads_created_count` | >= 2 |
| 4 | Hit Any Feature Limit 2x | `daily_limit_hit_count` | >= 2 |
| 5 | Hit 200 XP | `total_xp` | >= 200 |
| 6 | Joined or Created Challenge | `challenges_joined_count + challenges_created_count` | >= 1 |
| 7 | Started 6 Lessons | `lessons_started_count` | >= 6 |

**Segment name:** `S-EXCLUSIVE — Qualified for Exclusive Offer`
**Segment logic:** All 7 conditions AND `exclusive_offer_sent != true` (one-time per user)

### Flow

```
Entry (Segment: S-EXCLUSIVE)
  → Attribute Update: exclusive_offer_sent = true
  → Attribute Update: exclusive_offer_expires_at = {{now | plus: 86400}}
  → Email: "🔒 Exclusive 24h Offer — Unlocked by YOU, {{kid_name}}"
      ↳ Email has "Redeem Now" CTA button → deep link: getxplain://offer/redeem?token={{customer.id}}
      ↳ Tracked link on "Redeem" button
  → Wait Until: clicked email (Redeem link) OR 24h timeout
      ├─ CLICKED (redeemed):
      │   → Attribute Update: offer_redeemed = true
      │   → Attribute Update: offer_redeem_deadline = {{now | plus: 10800}}
      │   → Push: "⏰ Offer activated! You have 3 hours to subscribe"
      │   → Delay 1.5h
      │   → T/F Branch: is_subscribed = true?
      │       ├─ YES → Push "Welcome to Premium! 🎉" → Exit
      │       └─ NO → Push "90 minutes left! Don't lose your exclusive deal ⏳"
      │           → Delay 1h
      │           → T/F Branch: is_subscribed = true?
      │               ├─ YES → Push "Welcome to Premium! 🎉" → Exit
      │               └─ NO → Push "⏰ Final 30 min — this deal disappears forever"
      │                   → Delay 30min
      │                   → Attribute Update: offer_expired = true
      │                   → Exit
      └─ TIMEOUT (24h, didn't click):
          → Attribute Update: offer_expired = true
          → Push: "Your exclusive offer expired. Keep learning — you might unlock another one day 💜"
          → Exit
```

### Email Copy

**Subject:** {kid_name}, you unlocked something special 🔓
**Preheader:** 24 hours only. You earned this.

**Body:**
```
Hey {kid_name}! 🎉

You've done something only the best learners do:
✅ 5-day streak
✅ 3 lessons completed
✅ Joined squads & challenges
✅ Hit 200 XP
✅ Explored 6+ lessons

Because of that, we're giving YOU an exclusive deal:

🔒 [PREMIUM — 50% OFF]
This offer expires in 24 hours.
It ONLY works if you tap the button below.

[🎁 REDEEM MY OFFER]

After you redeem, you'll have 3 hours to subscribe.
This offer will NEVER appear again.

— The GetXplain Team
```

### Push Sequence

| When | Push Title | Push Body |
|------|-----------|-----------|
| On email send | 📧 Check your email, {kid_name}! | You just unlocked an exclusive offer. Open your email to see it! |
| On redeem click | ⏰ Offer activated! | You have 3 hours to subscribe at 50% off. Don't wait! |
| 1.5h after redeem | 90 min left! | Your exclusive 50% off Premium ends soon, {kid_name} ⏳ |
| 2.5h after redeem | Final 30 minutes! | ⏰ This is it — your exclusive deal disappears in 30 min |
| On subscribe | Welcome to Premium! 🎉 | You made the smartest choice, {kid_name}. Let's go! 🚀 |
| On 24h expiry | Offer expired 💜 | Keep learning — legends always get another chance |

### Key Attributes (Basel must implement)

```
exclusive_offer_sent          // bool — set true when offer fires (prevents re-send)
exclusive_offer_expires_at    // timestamp — 24h from send
offer_redeemed                // bool — clicked Redeem in email
offer_redeem_deadline         // timestamp — 3h from redeem click
offer_expired                 // bool — didn't convert in time
is_subscribed                 // bool — completed subscription
```

### Rules

- **One-time only** — `exclusive_offer_sent = true` prevents re-entry forever
- **Bypasses 2 email/day cap** — tagged as exclusive/transactional
- **Respects 5 push/day** — sends max 4 pushes in worst case (notify + 3 countdown)
- **Working hours enforced** — time window on entry
- **Tracked link required** — "Redeem" button must be a tracked link so Wait Until can detect the click

---

## MORE CAMPAIGN IDEAS (10 per category)

### A+. Sales/Subscriptions (21–30)

| # | Campaign | Description | Impact |
|---|----------|-------------|--------|
| A21 | **Post-Exclusive-Offer Follow-Up** | 7 days after expired exclusive offer: "You almost unlocked Premium last time. Here's what Premium users did this week: {stats}." Regret seeding. | 🔥🔥🔥 |
| A22 | **Parent Comparison Email** | "Kids with Premium generate 3x more lessons and have 2x longer streaks. Here's {kid_name}'s potential." Data-backed parent pitch. | 🔥🔥🔥 |
| A23 | **Squad Premium Bundle** | Squad creator + 3 active members: "Upgrade your whole squad — group discount. Premium squads get exclusive badges + squad challenges." | 🔥🔥🔥 |
| A24 | **XP Ceiling Breaker** | Users stuck at same XP range for 14+ days: "Premium 2x XP weekends could break you through. One weekend = what takes 2 weeks." | 🔥🔥 |
| A25 | **Generation Addict Conversion** | Users who hit daily limit 5+ times total: "You keep maxing out. Premium = unlimited. Your brain wants more — let it." | 🔥🔥🔥🔥 |
| A26 | **School Year Kickoff Offer** | September 1–15: email to all parents. "New year, unlimited learning. 40% off annual plan. {kid_name}'s classmates are already upgrading." | 🔥🔥🔥 |
| A27 | **Premium Preview Day** | Give free users 24h of premium features: "Today you have unlimited generation. See what Premium feels like." Then convert after taste. | 🔥🔥🔥🔥 |
| A28 | **Creator Monetization Tease** | For 50+ lesson creators: "Premium creators will soon earn rewards for popular lessons. Get early access." Future feature as hook. | 🔥🔥🔥 |
| A29 | **Challenge Loss → Premium Pitch** | After 3+ challenge losses: "Premium members get challenge analytics — see where you lost and how to win next time." Solve their pain. | 🔥🔥 |
| A30 | **Milestone Gate** | At 500 XP: "You've outgrown free mode, {kid_name}. The next level of learning is Premium." Positioned as graduation, not paywall. | 🔥🔥🔥 |

### B+. Engagement (21–30)

| # | Campaign | Description | Impact |
|---|----------|-------------|--------|
| B21 | **Cross-World Pollination** | Users who excel in one world: "You crushed {world_A}! Did you know {world_B} has similar lessons? Try one!" Expand breadth. | 🔥🔥🔥 |
| B22 | **Daily Lesson Digest** | Morning push: "Today's top 3 lessons by kids your age: {titles}. Which one will you try?" Curated content. | 🔥🔥🔥 |
| B23 | **Creator Streak** | Track consecutive days of generation: "You've generated lessons 3 days in a row! Keep your Creator Streak going!" New streak type. | 🔥🔥🔥🔥 |
| B24 | **Squad vs Squad Weekly** | Every Monday: "This week's rival squad: {rival_name} with {xp} XP. Can your squad beat them?" Inter-squad competition. | 🔥🔥🔥 |
| B25 | **Accuracy Improvement Tracker** | "Your accuracy went from 60% to 78% this month! At this rate, you'll hit 90% by {date}." Progress visualization. | 🔥🔥 |
| B26 | **Feature Unlock Progression** | "You've used 4 of 8 features. Try {unused_feature} to unlock the Explorer badge!" Gamified feature adoption. | 🔥🔥🔥 |
| B27 | **Weekly Goal Setter** | Monday push: "Set your goal: how many lessons this week? 3? 5? 10?" Then track and celebrate Friday. Self-commitment device. | 🔥🔥🔥 |
| B28 | **Lesson Rating Feedback Loop** | When lesson gets rated: "Your '{title}' got a ⭐⭐⭐⭐ rating! Create another one to beat your score." Quality motivation. | 🔥🔥🔥 |
| B29 | **Night Owl Redirect** | Users active after 9pm: morning push next day: "We saw you last night! Here's a fresh {world} lesson for today 🌅" Re-engage safely in working hours. | 🔥🔥 |
| B30 | **100-Day Club** | At 100 days since signup + still active: "You're in the 100-Day Club! Only {%} of kids make it here." Exclusive milestone. | 🔥🔥🔥 |

### C+. Retention (21–30)

| # | Campaign | Description | Impact |
|---|----------|-------------|--------|
| C21 | **Micro-Win Re-entry** | Day 4 inactive: "Just open the app and check your rank — takes 10 seconds." Lowest possible ask. | 🔥🔥🔥🔥 |
| C22 | **Lesson Saved By Others** | "While you were away, {count} kids saved your lessons to their backpacks!" Content has lasting value. | 🔥🔥🔥 |
| C23 | **Squad Rank Emergency** | If user's squad dropped 5+ ranks: "🚨 {squad_name} fell from #{old} to #{new}! They need you NOW." Urgency + obligation. | 🔥🔥🔥🔥 |
| C24 | **Partial Lesson Completion** | For users who answered 4/6 questions: "You were SO close! Just {remaining} questions left on '{title}'." Near-finish pull. | 🔥🔥🔥 |
| C25 | **Birthday Week Reactivation** | Week of kid's birthday: "🎂 Birthday bonus! Double XP all week for {kid_name}. Come celebrate!" Timely + generous. | 🔥🔥🔥 |
| C26 | **Same-School Rival Push** | "{school_rival_name} from {school} just passed your rank. Are you going to let a classmate beat you?" Hyper-local competition. | 🔥🔥🔥🔥 |
| C27 | **"Your Fans Miss You" Creator Push** | For creators with followers: "{followers_count} fans are waiting for your next lesson. What will you teach them?" Identity-based. | 🔥🔥🔥 |
| C28 | **Day 5 Voice Note Push** | Push with audio preview (if supported): "Tap to hear what {friend_name} learned today!" Novel format breaks notification blindness. | 🔥🔥 |
| C29 | **Streak Ghost Recovery** | Streak broke 3-7 days ago: "Your old {old_streak}-day streak was legendary. Start the sequel today — Day 1 of an even bigger one." Reframe. | 🔥🔥🔥 |
| C30 | **Parent Weekend Digest** | Saturday email to parent of 5+ day inactive kid: "{kid_name}'s friends are learning this weekend. 15 minutes could restart their streak." Weekend context. | 🔥🔥🔥 |

### D+. Reacquisition (21–30)

| # | Campaign | Description | Impact |
|---|----------|-------------|--------|
| D21 | **App Update Push (re-install)** | If push token invalid (likely uninstalled): email "GetXplain just got a huge update. Reinstall and get a Comeback bonus!" Only channel left. | 🔥🔥🔥🔥 |
| D22 | **Classroom Integration Announcement** | "GetXplain is now used by {count} schools in {country}. {kid_name}'s school might be next — be ready!" FOMO + authority. | 🔥🔥🔥 |
| D23 | **"We Made This For You" Personalized World** | "Based on {kid_name}'s past lessons, we curated a {favorite_world} starter pack. 3 lessons picked just for them." Personal relevance. | 🔥🔥🔥🔥 |
| D24 | **Parent Testimonial Email** | "Here's what other parents say: '{testimonial}'. Give {kid_name} another chance at active learning." Social proof to decision-maker. | 🔥🔥🔥 |
| D25 | **Expiring Profile Warning** | 90-day email: "{kid_name}'s progress may be archived soon: {xp} XP, {lessons} lessons, #{rank}. Log in to keep it." Loss aversion. | 🔥🔥🔥🔥 |
| D26 | **New Challenge Type Announcement** | When new feature ships: "New: Team Challenges! Bring friends and compete together. {kid_name}'s squad is waiting." Feature-driven comeback. | 🔥🔥🔥 |
| D27 | **Annual Achievement Certificate** | Year-end email: PDF certificate of kid's achievements. "Print {kid_name}'s GetXplain Certificate of Learning. Come back to earn next year's!" Tangible. | 🔥🔥🔥 |
| D28 | **WhatsApp Re-engagement** | 60-day+, email dead: WhatsApp to parent number: "Hi {parent_name}! {kid_name}'s GetXplain friends miss them. Quick tap to reopen 👇" | 🔥🔥🔥🔥 |
| D29 | **School Break Blitz** | Mid-year/summer break: "No homework, all fun! {kid_name} can explore any topic freely. 5 lessons/day, zero stress." Reposition as entertainment. | 🔥🔥🔥 |
| D30 | **Founder Video Message** | Email with embedded video from Tarek: "Hi, I'm Tarek, founder of GetXplain. I built this for kids like {kid_name}..." Most personal touch possible. | 🔥🔥🔥🔥 |
