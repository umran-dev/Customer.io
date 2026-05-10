# GetXplain.AI — Extended Campaign Ideas + Exclusive Offer System

## Product Model

| Feature | Freemium | Premium |
|---------|----------|---------|
| Kid Profiles | 2 max | 6 max |
| Library Lessons (from Worlds) | 3/day | Unlimited |
| AI Generation | 3/day | 12/day |
| Squads | ❌ Locked | ✅ Full access |
| Challenges | 2/day | Unlimited |

- **No trial** — all conversion through value demonstration, not time-gated
- Limits reset daily

## Updated Rules

- Max **5 push/day** per user
- Max **2 emails/day** per user
- **Exception:** Exclusive Offer emails bypass the 2 email/day cap (tagged as transactional/exclusive)
- Working hours: 9am–9pm Cairo (Africa/Cairo)
- Exit on goal hit

---

## S0. THE EXCLUSIVE 24H OFFER (Priority Sales Campaign)

### Trigger Conditions (ALL must be true)

| # | Condition | Attribute | Check | Note |
|---|-----------|-----------|-------|------|
| 1 | 5-Day Streak | `current_streak_days` | >= 5 | Proves daily habit |
| 2 | Finished 3 Library Lessons | `lessons_completed_count` | >= 3 | Hit library cap at least once |
| 3 | Created or Joined Squad 2x | `squads_joined_count + squads_created_count` | >= 2 | Must be Premium to do this — so this condition only fires for Premium users OR is removed for free users who can't access squads |
| 4 | Hit Any Feature Limit 2x | `daily_limit_hit_count` | >= 2 | Felt the friction (AI 3/day, library 3/day, or challenge 2/day) |
| 5 | Hit 200 XP | `total_xp` | >= 200 | Invested enough to value upgrade |
| 6 | Joined or Created Challenge | `challenges_joined_count + challenges_created_count` | >= 1 | Used competitive features |
| 7 | Started 6 Lessons | `lessons_started_count` | >= 6 | Explored broadly |

> **Note on condition #3 (Squads):** Since Squads are Premium-only, replace this for free users with: `challenges_created_count + challenges_joined_count >= 3` (used social/competitive features more heavily). Or remove it entirely for the free-user segment — the other 6 conditions still prove high engagement.

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
| A21 | **Post-Exclusive-Offer Follow-Up** | 7 days after expired offer: "You almost unlocked Premium. This week Premium users created 4x more lessons. You're still stuck at 3/day." Regret + specific numbers. | 🔥🔥🔥 |
| A22 | **Parent Limit Report** | "This week {kid_name} hit their AI limit {x} times, library limit {y} times, challenge limit {z} times. Premium removes all of them: 12 AI, unlimited library, unlimited challenges." Data-backed. | 🔥🔥🔥🔥 |
| A23 | **Squad Invitation Wave** | When 3+ friends of a free user are in squads: "Your friends are in squads competing together. Squads are Premium-only — upgrade to join them." Social exclusion pressure. | 🔥🔥🔥🔥 |
| A24 | **Rank Stall + Limit Connection** | Stuck at rank 14+ days: "Your rank isn't moving. Free = 3 AI + 3 library + 2 challenges/day. Premium users earn 4x more XP daily. That's why they're above you." Cause → effect. | 🔥🔥🔥 |
| A25 | **All-Limits-Hit Streak** | User hits all 3 limits (AI + library + challenge) for 3 consecutive days: "3 days in a row you maxed out everything. You've outgrown free. Premium was made for kids like you." Chronic pattern. | 🔥🔥🔥🔥 |
| A26 | **Family Growth Trigger** | Parent attempts 3rd profile: "Your family is growing! Premium supports 6 kid profiles — one subscription, whole family. Every child deserves to learn." | 🔥🔥🔥🔥 |
| A27 | **Limit Reset Anticipation** | Push at 11:59pm to users who hit limits: "Limits reset at midnight. Free: 3 AI, 3 library, 2 challenges. Premium: 12 AI, unlimited library, unlimited challenges. Upgrade before tomorrow." | 🔥🔥🔥 |
| A28 | **Creator Monetization Tease** | 50+ lesson creators: "Premium creators will earn rewards for popular lessons. Get early access — plus 12 AI generations/day to create even more." Future + utility. | 🔥🔥🔥 |
| A29 | **Challenge Loss + Cap Combo** | 3+ challenge losses AND hit 2/day challenge cap: "You lost and couldn't practice more — capped at 2 challenges. Premium = unlimited challenges. Train and win." | 🔥🔥🔥 |
| A30 | **Both Kids Active → Family Pitch** | Both profiles active 5+ days: "Both {kid1} and {kid2} love GetXplain! Premium: 6 profiles, 12 AI lessons, squads, unlimited challenges. One price, whole family." | 🔥🔥🔥🔥 |

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
