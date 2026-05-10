# GetXplain.AI — Master Campaign Funnel

> Impact: 🔥 low, 🔥🔥 medium, 🔥🔥🔥 high, 🔥🔥🔥🔥 critical

## Product Model

| Feature | Freemium | Premium |
|---------|----------|---------|
| Kid Profiles | 2 max | 6 max |
| Library Lessons (from Worlds) | 3/day | Unlimited |
| AI Generation | 3/day | 12/day |
| Squads | ❌ Locked | ✅ Full access |
| Challenges | 2/day | Unlimited |

No trial. Limits reset daily.

## Rules

- Max **5 push/day**, **2 emails/day** per user
- **Exception:** Exclusive Offer emails bypass email cap
- Working hours: **9am–9pm Cairo** (Africa/Cairo)
- Exit immediately on goal hit
- 80% kid / 20% parent messaging

## Funnel

```
ONBOARDING → ENGAGEMENT → SALES → RETENTION → REACQUISITION
  (Day 0-7)   (Active)    (Convert)  (Slipping)    (Churned)
```

---

# 1. ONBOARDING (Day 0–7 — Turn signups into active users)

**Goal:** Get new user from signup → first lesson completed → first lesson generated → daily habit formed within 7 days.

| # | Campaign | Description | Impact |
|---|----------|-------------|--------|
| O1 | **Welcome Email from Tarek** | Immediate after signup. Personal email from Tarek to parent: "Hi {parent_name}, I'm Tarek, the founder of GetXplain. Thank you for signing {kid_name} up — here's what they can do: generate AI lessons on any topic, explore 8 worlds, compete in challenges, and climb leaderboards. Their first lesson is one tap away." CTA deep links to Worlds browser. Sets tone: founder cares, real human behind the app. Kid gets push: "Welcome, {kid_name}! 🎉 Tap to start your first lesson!" | 🔥🔥🔥🔥 |
| O2 | **Day 1 — First AI Generation Nudge** | 24h after signup, if lessons_generated_count = 0: push "You haven't created your own lesson yet! Type any topic, snap a photo, or use your voice — the AI builds a lesson just for you ✨" Introduces the core action. | 🔥🔥🔥🔥 |
| O3 | **Day 2 — Streak Starter** | 48h after signup, if current_streak_days < 2: push "Come back today and start a streak! 🔥 Day 2 = the beginning of something big." If streak = 2: "2 days in a row! Keep going tomorrow for Day 3!" Introduces streak mechanic. | 🔥🔥🔥🔥 |
| O4 | **Day 3 — World Explorer** | 72h after signup, if worlds_visited_count <= 1: push "You've only tried {world}! There are 8 worlds to explore — try {suggested_world} today. Kids your age love it 🌍" Broadens usage beyond first world. | 🔥🔥🔥 |
| O5 | **Day 5 — Social Features Intro** | 5 days after signup: push "Did you know you can challenge your friends? 🥊 Create a challenge and share the code — see who knows more!" Introduces challenges (free: 2/day). If has followers: mention leaderboard rank. | 🔥🔥🔥 |
| O6 | **Day 7 — First Week Celebration + Habit Lock** | 7 days after signup. Push: "One week on GetXplain! 🏆 You've earned {total_xp} XP and completed {lessons_completed_count} lessons. Keep your streak alive — legends are built daily!" Email to parent: "{kid_name}'s first week report" with stats. Sets expectation for ongoing engagement. | 🔥🔥🔥🔥 |

---

# 2. ENGAGEMENT (Keep active users active all year)

**Goal:** 60% of effort — maintain daily/weekly activity, deepen feature usage, build social connections.

| # | Campaign | Description | Impact |
|---|----------|-------------|--------|
| E1 | **Daily Streak Protector** | Push at 5pm + 7pm Cairo when streak_at_risk. Personal best variant if about_to_hit_personal_best. *Already built in Customer.io (Campaign ID: 6).* | 🔥🔥🔥🔥 |
| E2 | **Weekly World Discovery** | Every Monday, suggest unvisited world by age/gender: "This week's adventure: {world}! 3 lessons = a new badge." Expands exploration. | 🔥🔥🔥 |
| E3 | **Daily Generation Reminder** | At user's most_active_hour: "Your 3 daily AI lessons are ready! What will you teach the world today?" Only for users who generated yesterday. Habit loop. | 🔥🔥🔥🔥 |
| E4 | **Friend Activity Nudge** | When followed user generates/completes: "Your friend {name} just created a lesson on {topic}!" Social proof drives action. | 🔥🔥🔥 |
| E5 | **Squad Weekly Recap** | Sunday push to squad members: "Your squad earned {xp} XP this week! You contributed {%}. Beat it next week?" Group accountability. (Premium only) | 🔥🔥🔥 |
| E6 | **Leaderboard Climb Celebration** | rank_climbed_today = true: "You jumped to #{rank}! #{rank-1} is only {xp_gap} XP away." Momentum reinforcement. | 🔥🔥🔥 |
| E7 | **XP Milestone Celebrations** | At 100, 500, 1000, 5000 XP: push + in-app. "You hit {milestone} XP! Only {%} of kids reach this level." Achievement dopamine. | 🔥🔥🔥 |
| E8 | **Challenge of the Day** | Daily 3:30pm push: "Today's challenge: Create a lesson about {trending_topic}!" Direction for undecided users. | 🔥🔥🔥🔥 |
| E9 | **Difficulty Upgrade Nudge** | 10+ Easy at 90%+ accuracy: "You're crushing Easy mode! Ready for Medium? 30 more XP per lesson." Skill progression. | 🔥🔥 |
| E10 | **Weekend Warrior Activation** | Saturday 10am to weekend_user: "Weekend = learning time! Explore {suggested_world} today." Predictable slot. | 🔥🔥 |
| E11 | **Lesson Impact Notification** | their_lessons_used_by_others increases: "3 more kids learned from your '{topic}' lesson!" Creator motivation loop. | 🔥🔥🔥🔥 |
| E12 | **Monthly Recap Email** | 1st of month: email to parent + push to kid. Stats, achievements, worlds explored. "Your {month} in review." | 🔥🔥🔥 |
| E13 | **Squad Challenge Kickoff** | squad_was_active but user 48h idle: "Your squad is on fire! They need your XP this week." (Premium only) | 🔥🔥🔥 |
| E14 | **New Badge Almost Unlocked** | 1 action from badge: "One more {action} and you unlock {badge_name}!" Near-completion drive. | 🔥🔥🔥 |
| E15 | **Method Variety Nudge** | Type-only users: "Snap a photo of anything and turn it into a lesson! 📸 Try it!" Feature discovery. | 🔥🔥 |
| E16 | **School Leaderboard Pride** | Top 10 school entry: "You're #{rank} in {school}! Your classmates can see your achievements." Local status. | 🔥🔥🔥 |
| E17 | **Bilingual Challenge** | Single-language users: "Try {other_language}! Bilingual creators earn a special badge." Content diversity. | 🔥🔥 |
| E18 | **Seasonal Content Themes** | Ramadan, National Day, Summer Science: "Create a lesson about {seasonal_topic}!" Freshness. | 🔥🔥🔥 |
| E19 | **Follow Suggestion Engine** | 0 follows: "Kids who follow friends generate 2x more lessons. Find your classmates!" Social glue. | 🔥🔥 |
| E20 | **Personal Best Streak Celebration** | beat_personal_best_today: "NEW RECORD! {days}-day streak! You're unstoppable!" Positive reinforcement. | 🔥🔥🔥 |
| E21 | **Cross-World Pollination** | Excel in one world: "You crushed {world_A}! {world_B} has similar lessons — try one!" Breadth. | 🔥🔥🔥 |
| E22 | **Daily Lesson Digest** | Morning: "Top 3 lessons by kids your age: {titles}. Which one will you try?" Curated content. | 🔥🔥🔥 |
| E23 | **Creator Streak** | Consecutive generation days: "3 days creating in a row! Keep your Creator Streak going!" New streak type. | 🔥🔥🔥🔥 |
| E24 | **Squad vs Squad Weekly** | Monday: "Rival squad: {rival_name} with {xp} XP. Beat them?" Inter-squad competition. (Premium only) | 🔥🔥🔥 |
| E25 | **Accuracy Improvement Tracker** | "Accuracy: 60% → 78% this month! At this rate, 90% by {date}." Progress visualization. | 🔥🔥 |
| E26 | **Feature Unlock Progression** | "Used 4 of 8 features. Try {unused_feature} for the Explorer badge!" Gamified adoption. | 🔥🔥🔥 |
| E27 | **Weekly Goal Setter** | Monday: "How many lessons this week? 3? 5? 10?" Track and celebrate Friday. Self-commitment. | 🔥🔥🔥 |
| E28 | **Lesson Rating Feedback Loop** | Lesson rated: "Your '{title}' got ⭐⭐⭐⭐! Create another one to beat your score." Quality motivation. | 🔥🔥🔥 |
| E29 | **Night Owl Redirect** | Active after 9pm → morning push: "Fresh {world} lesson for today 🌅" Re-engage in working hours. | 🔥🔥 |
| E30 | **100-Day Club** | 100 days + still active: "You're in the 100-Day Club! Only {%} of kids make it here." Milestone. | 🔥🔥🔥 |

---

# 3. SALES (Convert free → paid)

**Goal:** 40% of effort — convert engaged free users to Premium using friction points, social pressure, and value demonstration.

### S0. THE EXCLUSIVE 24H OFFER

**Trigger:** ALL conditions true + `exclusive_offer_sent != true`:

| Condition | Check |
|-----------|-------|
| 5-Day Streak | `current_streak_days >= 5` |
| 3 Library Lessons | `lessons_completed_count >= 3` |
| Hit Any Limit 2x | `daily_limit_hit_count >= 2` |
| 200 XP | `total_xp >= 200` |
| 1+ Challenge | `challenges_joined_count + challenges_created_count >= 1` |
| 6+ Lessons Started | `lessons_started_count >= 6` |

**Flow:**
```
Entry → Set exclusive_offer_sent = true
  → Email "🔒 Exclusive 24h Offer" (bypasses 2/day cap)
  → Push "📧 Check your email!"
  → Wait Until: clicked Redeem OR 24h timeout
    ├─ CLICKED → Set offer_redeemed = true
    │   → Push "⏰ 3 hours to subscribe!"
    │   → 1.5h delay → Branch: subscribed?
    │       ├─ YES → Push "Welcome to Premium! 🎉" → Exit
    │       └─ NO → Push "90 min left!"
    │           → 1h delay → Branch: subscribed?
    │               ├─ YES → Push "Welcome! 🎉" → Exit
    │               └─ NO → Push "Final 30 min!" → 30min → Set expired → Exit
    └─ TIMEOUT → Set expired → Push "Offer expired 💜" → Exit
```
One-time only. Tracked link on Redeem button.

### S1–S30 Campaigns

| # | Campaign | Description | Impact |
|---|----------|-------------|--------|
| S1 | **AI Generation Limit Wall** | Hit 3/day AI cap: "All 3 AI lessons used. Premium = 12/day — 4x more creating power." Highest-intent moment. | 🔥🔥🔥🔥 |
| S2 | **Library Lesson Cap Hit** | Hit 3/day library cap: "3 library lessons done! Premium = unlimited library. Never stop learning." | 🔥🔥🔥🔥 |
| S3 | **Parent Value Report → Upsell** | Monthly email: stats + "hit limits {count} times. Premium: 12 AI, unlimited library, squads, unlimited challenges." | 🔥🔥🔥🔥 |
| S4 | **3rd Child Profile Wall** | Attempt 3rd profile: "Free = 2 profiles. Premium = 6. Every child deserves to learn." Friction-point. | 🔥🔥🔥🔥 |
| S5 | **Sibling FOMO Trigger** | 2 profiles both active: "Both kids love it. Got more? Premium = 6 profiles, one account." | 🔥🔥🔥🔥 |
| S6 | **Squad Teaser** | Free user sees squad content: "Squads are Premium! Join friends, compete as a team." Social glue behind paywall. | 🔥🔥🔥🔥 |
| S7 | **Squad Invite Rejection** | Free user gets squad invite, can't join: "Your friend invited you! Squads = Premium-only. Upgrade to join." Peak social pressure. | 🔥🔥🔥🔥 |
| S8 | **Challenge Limit Hit** | Hit 2/day cap: "2 challenges done — want more! Premium = unlimited challenges." Competition-driven. | 🔥🔥🔥 |
| S9 | **Feature Gate Tap** | Taps premium feature: in-app listing all premium benefits with specific numbers. Contextual. | 🔥🔥🔥🔥 |
| S10 | **Power Creator Upgrade** | Hit AI limit 5+ times total: "Capped {count} times = {count×9} lessons never created. Premium = 12/day." Quantified loss. | 🔥🔥🔥🔥 |
| S11 | **Famous Creator Verification** | 20+ others used lessons: "You teach hundreds — but 3/day limits you. Premium: 12/day + Verified badge." | 🔥🔥🔥 |
| S12 | **Challenge Addict Conversion** | Challenge cap 3+ consecutive days: "You love competing! Free = 2/day. Premium = unlimited." Pattern-based. | 🔥🔥🔥 |
| S13 | **Triple Limit Day** | Hit AI + library + challenge limits same day: "You maxed EVERYTHING. You've outgrown free." Ultimate frustration. | 🔥🔥🔥🔥 |
| S14 | **Leaderboard Ceiling Breaker** | Stuck rank 11-50 for 7+ days: "3 lessons/day caps your XP. Premium = 4x more daily." | 🔥🔥🔥 |
| S15 | **Social Proof Email** | Monthly: "{X} families in {country} upgraded. Top reasons: 12 AI/day, squads, unlimited challenges." | 🔥🔥 |
| S16 | **Back-to-School Annual** | September: "Premium: 12 AI/day, unlimited library, squads, 6 profiles. 40% off annual." | 🔥🔥🔥 |
| S17 | **Tarek Personal Offer** | 30 days active + free: "You hit limits {count} times. I want to remove them — 30% off." One-time. | 🔥🔥🔥 |
| S18 | **Abandoned Upgrade Retarget** | Viewed pricing, didn't convert: "12 AI. Unlimited library. Squads. Unlimited challenges. 6 profiles. That's Premium." | 🔥🔥🔥🔥 |
| S19 | **Exam Season Push** | Before exams: "3/day isn't enough for exam prep. Premium = 12 AI + unlimited library." | 🔥🔥🔥 |
| S20 | **Gifting Campaign** | Eid/Ramadan/holidays: "Gift Premium for the family (6 kids, 12 AI/day, squads). 25% off." | 🔥🔥🔥 |
| S21 | **Post-Exclusive Follow-Up** | 7d after expired offer: "You almost unlocked Premium. Still stuck at 3/day." Regret. | 🔥🔥🔥 |
| S22 | **Parent Limit Report** | Weekly: "AI limit hit {x}x, library {y}x, challenge {z}x. Premium removes all." Data-backed. | 🔥🔥🔥🔥 |
| S23 | **Squad Invitation Wave** | 3+ friends in squads: "Your friends compete in squads. Squads = Premium-only." Social exclusion. | 🔥🔥🔥🔥 |
| S24 | **Rank Stall + Limits** | Stuck 14+ days: "Free = 3+3+2/day. Premium users earn 4x more XP daily. That's why they're above you." | 🔥🔥🔥 |
| S25 | **All-Limits Streak** | All 3 limits for 3 consecutive days: "3 days maxing everything. Premium was made for you." Chronic pattern. | 🔥🔥🔥🔥 |
| S26 | **Family Growth Trigger** | Attempt 3rd profile: "Family growing! Premium = 6 profiles, one subscription." | 🔥🔥🔥🔥 |
| S27 | **Limit Reset Anticipation** | 11:59pm to limit-hitters: "Limits reset at midnight. Free: 3/3/2. Premium: 12/unlimited/unlimited." | 🔥🔥🔥 |
| S28 | **Creator Monetization Tease** | 50+ lessons: "Premium creators earn rewards for popular lessons. Get early access + 12/day." | 🔥🔥🔥 |
| S29 | **Challenge Loss + Cap** | 3+ losses AND hit 2/day cap: "Lost and can't practice more. Premium = unlimited challenges." | 🔥🔥🔥 |
| S30 | **Both Kids Active Family Pitch** | Both profiles active 5+ days: "Both love it! Premium: 6 profiles, 12 AI, squads, unlimited. One price." | 🔥🔥🔥🔥 |

---

# 4. RETENTION (Inactive users → active again)

**Goal:** Re-engage users who stopped using the app (3–21 days inactive) before they churn.

| # | Campaign | Description | Impact |
|---|----------|-------------|--------|
| R1 | **Day 3 Soft Nudge** | Push using favorite_world: "New {favorite_world} lessons are waiting, {kid_name}." Gentle, relevant. | 🔥🔥🔥🔥 |
| R2 | **Day 5 Streak Loss Reframe** | "Your {old_streak}-day streak is gone — but starting fresh takes just one lesson." Loss → opportunity. | 🔥🔥🔥 |
| R3 | **Day 7 Stats Email** | Email: "{kid_name} built {lessons} lessons, {xp} XP, {streak} best streak. Come back and keep building!" Nostalgia. | 🔥🔥🔥🔥 |
| R4 | **Day 7 Friend Activity Hook** | "{friend_name} created 5 lessons while you were away. See what they're learning!" Social pull. | 🔥🔥🔥🔥 |
| R5 | **Abandoned Lesson Recovery** | "You left '{title}' at {progress}%. Just {remaining} questions left!" Sunk cost + near-completion. | 🔥🔥🔥 |
| R6 | **Squad Missing You** | "Your squad '{squad_name}' dropped to #{rank}. They need your XP!" Group obligation. (Premium) | 🔥🔥🔥🔥 |
| R7 | **Pending Challenge Reminder** | Escalating: "Someone challenged you!" → 6h "Waiting..." → 18h "Expires soon!" | 🔥🔥🔥 |
| R8 | **New Content in Favorite World** | "{{count}} new {favorite_world} lessons since you last visited!" Pull content. | 🔥🔥🔥 |
| R9 | **Rank Drop Alert** | "You fell from #{old} to #{new}. One lesson gets you back." Loss aversion. | 🔥🔥🔥🔥 |
| R10 | **Power User VIP Save** | power_user + 3d inactive: push about rank → 48h Tarek email to parent. High-touch. | 🔥🔥🔥🔥 |
| R11 | **Generator Block Breaker** | Creator 3+ days no generation: "Your fans are waiting — {count} kids learned from you!" Creator identity. | 🔥🔥🔥 |
| R12 | **Day 10 Curiosity Ping** | "Kids are creating lessons about {trending_topic}. What would you create?" Curiosity hook. | 🔥🔥 |
| R13 | **Weekend Comeback Special** | Friday push, 4-6 day gap: "Weekend = explore {new_world}. Your streak restarts with one lesson." | 🔥🔥🔥 |
| R14 | **School Leaderboard Urgency** | Was top 10 school, slipped: "You were #{old} at {school} — classmates are catching up!" Local pride. | 🔥🔥🔥 |
| R15 | **Follower Miss-You** | "{followers_count} kids follow you. Show them what you've got!" Identity as creator. | 🔥🔥 |
| R16 | **Method Re-engagement** | "Last time you used 📸 photo mode on {topic}. Try it again with something new!" Memory trigger. | 🔥🔥 |
| R17 | **Day 14 Parent Email** | "Hi {parent_name}, {kid_name} hasn't been on in 2 weeks. Kids who learn daily score 40% higher." | 🔥🔥🔥🔥 |
| R18 | **Challenge Win Streak Reminder** | "You won {wins} challenges! A new opponent is waiting." Past success recall. | 🔥🔥 |
| R19 | **Personalized World Recommendation** | Age + gender + history: "We think you'd love {world}. 95% of kids your age enjoy it!" | 🔥🔥🔥 |
| R20 | **Day 14 Last Push Bundle** | Multi-channel: Push + Email + In-App. "We saved your progress. Your rank. Your squad. All still here." | 🔥🔥🔥🔥 |
| R21 | **Micro-Win Re-entry** | Day 4: "Just check your rank — takes 10 seconds." Lowest possible ask. | 🔥🔥🔥🔥 |
| R22 | **Lesson Saved By Others** | "While you were away, {count} kids saved your lessons!" Content has lasting value. | 🔥🔥🔥 |
| R23 | **Squad Rank Emergency** | Squad dropped 5+ ranks: "🚨 {squad_name} fell from #{old} to #{new}! They need you NOW." (Premium) | 🔥🔥🔥🔥 |
| R24 | **Partial Lesson Completion** | Answered 4/6 questions: "SO close! Just {remaining} left on '{title}'." Near-finish pull. | 🔥🔥🔥 |
| R25 | **Birthday Week Reactivation** | Birthday week: "🎂 Double XP all week for {kid_name}!" Timely + generous. | 🔥🔥🔥 |
| R26 | **Same-School Rival Push** | "{rival} from {school} just passed your rank. Let a classmate beat you?" Hyper-local. | 🔥🔥🔥🔥 |
| R27 | **"Your Fans Miss You"** | Creators with followers: "{count} fans waiting for your next lesson." Identity. | 🔥🔥🔥 |
| R28 | **Day 5 Voice Note Push** | Audio preview if supported: "Hear what {friend_name} learned today!" Novel format. | 🔥🔥 |
| R29 | **Streak Ghost Recovery** | Streak broke 3-7d ago: "Your {old_streak}-day streak was legendary. Start the sequel — Day 1!" Reframe. | 🔥🔥🔥 |
| R30 | **Parent Weekend Digest** | Saturday email, 5+ day gap: "{kid_name}'s friends learn this weekend. 15 min restarts their streak." | 🔥🔥🔥 |

---

# 5. REACQUISITION (Churned / uninstalled users → comeback)

**Goal:** Win back users gone 21+ days or who uninstalled. Email + SMS/WhatsApp primary channels (push may not work).

| # | Campaign | Description | Impact |
|---|----------|-------------|--------|
| Q1 | **Day 21 Tarek Personal Email** | Tarek to parent: "I noticed {kid_name} hasn't been on. We've added {features} since. I'd love them back." Founder touch. | 🔥🔥🔥🔥 |
| Q2 | **"We've Changed" Update Email** | After major update: "Big upgrade: {feature_list}. Come see what's new!" Product news as reactivation. | 🔥🔥🔥🔥 |
| Q3 | **Nostalgia Stats Email** | "{kid_name}'s Legacy: {xp} XP, {lessons} lessons, {streak} longest streak. Still helping other kids learn." Emotional. | 🔥🔥🔥🔥 |
| Q4 | **Friend Still Active** | "{friend_name} is at #{rank} now. Come back and see what you're missing." Social comparison. | 🔥🔥🔥 |
| Q5 | **Squad Needs You** | "Your squad '{name}' is still competing at #{rank}. One more member could push them higher." (Premium) | 🔥🔥🔥 |
| Q6 | **Seasonal Re-engagement** | Ramadan/Summer/Back-to-school: timely learning hooks matched to cultural moments. | 🔥🔥🔥 |
| Q7 | **New World Announcement** | "A brand new world just landed: {world}! Be one of the first to explore." Exclusive novelty. | 🔥🔥🔥🔥 |
| Q8 | **Your Lessons Are Still Famous** | "While you were gone, {count} more kids learned from your lessons!" Legacy pride. | 🔥🔥🔥🔥 |
| Q9 | **Comeback Challenge** | "Special Comeback Challenge: 3 lessons this week = bonus {xp} XP + Comeback badge." Incentive. | 🔥🔥🔥 |
| Q10 | **Parent Report Card** | "Kids {kid_name}'s age are exploring {topics}. Screen time that matters." Parent as re-entry driver. | 🔥🔥🔥 |
| Q11 | **Classmate Activity Digest** | "{count} kids from {school} active this week. {kid_name}'s school rank is waiting." School FOMO. | 🔥🔥🔥 |
| Q12 | **Streak Amnesty** | "Fresh start: come back this week, start with a 3-day streak bonus!" Removes loss barrier. | 🔥🔥🔥🔥 |
| Q13 | **Birthday Re-engagement** | Birthday: "🎂 Double XP for 24 hours. Come celebrate!" Personal + timely. | 🔥🔥🔥 |
| Q14 | **SMS/WhatsApp Final Reach** | 45+ days, email dead: SMS/WhatsApp to parent: "{kid_name}'s account is still active. Tap to reopen." | 🔥🔥🔥🔥 |
| Q15 | **Competitor-Proof Email** | "GetXplain = kids create lessons, not just watch. Active learning > passive videos." Differentiation to parent. | 🔥🔥 |
| Q16 | **Leaderboard Reset** | New quarter: "Everyone's at 0. This is your chance to be #1 in {city}." Fresh start. | 🔥🔥🔥🔥 |
| Q17 | **Referral Incentive** | "Come back + invite a friend = bonus XP + limited badge for both." Reactivation + growth. | 🔥🔥🔥 |
| Q18 | **School Partnership Trigger** | School adopts GetXplain: "Great news — {school} is using GetXplain! {kid_name} can earn school credit." | 🔥🔥🔥🔥 |
| Q19 | **Progress Preservation Warning** | 60-day: "We keep data 90 days. {xp} XP, {lessons} lessons, #{rank} still saved. After that, no guarantee." Loss. | 🔥🔥🔥 |
| Q20 | **"One Tap Comeback" Deep Link** | Email with button deep-linking into favorite world with suggested topic. Zero friction. | 🔥🔥🔥🔥 |
| Q21 | **App Update Reinstall** | Push token invalid (uninstalled): email "Huge update. Reinstall for Comeback bonus!" Only channel left. | 🔥🔥🔥🔥 |
| Q22 | **Classroom Integration** | "{count} schools in {country} use GetXplain. {kid_name}'s school might be next — be ready!" | 🔥🔥🔥 |
| Q23 | **Personalized Starter Pack** | "Curated {favorite_world} starter pack: 3 lessons picked just for {kid_name}." Personal relevance. | 🔥🔥🔥🔥 |
| Q24 | **Parent Testimonial** | "Other parents say: '{testimonial}'. Give {kid_name} another chance." Social proof to parent. | 🔥🔥🔥 |
| Q25 | **Expiring Profile Warning** | 90-day: "{kid_name}'s progress may be archived soon. Log in to keep it." Loss aversion. | 🔥🔥🔥🔥 |
| Q26 | **New Feature Announcement** | "New: {feature}! {kid_name}'s squad/friends are already using it." Feature-driven comeback. | 🔥🔥🔥 |
| Q27 | **Annual Achievement Certificate** | Year-end: PDF certificate of kid's achievements. "Come back to earn next year's!" Tangible. | 🔥🔥🔥 |
| Q28 | **WhatsApp Re-engagement** | 60d+, email dead: WhatsApp to parent: "{kid_name}'s friends miss them. Quick tap to reopen 👇" | 🔥🔥🔥🔥 |
| Q29 | **School Break Blitz** | Summer/mid-year break: "No homework, all fun! Explore any topic, zero stress." Reposition as entertainment. | 🔥🔥🔥 |
| Q30 | **Founder Video Message** | Email with video from Tarek: "I built this for kids like {kid_name}..." Most personal touch. | 🔥🔥🔥🔥 |
