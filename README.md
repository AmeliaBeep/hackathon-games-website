# 🎮 CheckPoint (hackathon-games-website)

CheckPoint is a blog-style web application focused on games.  
Users can create posts about their favorite titles, attach images, and interact with each other through three reactions.

---

## 👤 User Stories
- **As a visitor**, I want to **sign up for an account** so that I can create posts and react to others.  
- **As a user**, I want to **log in and log out** so that I can securely access my account.  
- **As a user**, I want to **create a post with a title, text, and image** so that I can share my thoughts about games.  
- **As a user**, I want to **view posts in a feed** so that I can see what others are saying about games.  
- **As a user**, I want to **edit my own posts** so that I can update or correct my content.  
- **As a user**, I want to **delete my own posts** so that I can remove content I no longer want to share.  
- **As a user**, I want to **react to posts with one of three reactions** so that I can engage with the community.  
- **As a user**, I want the **UI to be responsive** so that I can use the blog easily on mobile and desktop.  

---

## 🖥️ User Interface (UI)
- **Homepage / Feed**  
  Each post shows:
  - Username
  - Title
  - Image (scaled responsively to fit the feed)
  - Text content
  - Reactions
  - Datestamp

- **Navigation Bar**  
  Provides quick access to:
  - Home
  - Login
  - Sign Up

- **Authentication Pages**  
  Custom templates for login and signup, styled with Bootstrap.  
  Forms are centered and responsive for mobile and desktop.

---

## 🔧 CRUD Functions
- **Create**  
  Authenticated users can create a new post with:
  - Title
  - Text
  - Optional image upload (validated and resized to fit the feed)

- **Read**  
  All posts are displayed on the homepage feed.  
  Users can view posts with images, text, reactions, and timestamps.

- **Update**  
  Post owners can edit their own posts:
  - Change title
  - Update text
  - Replace image

- **Delete**  
  Post owners can delete their own posts.  
  Once deleted, the post is removed from the feed.

---

## 😀 Reactions
Each post supports **three reactions**.  
Users can click to react, and reaction counts update dynamically.

---

## ☁️ Cloudinary Integration
CheckPoint uses **Cloudinary** for media storage and delivery:
- User‑uploaded images are stored in Cloudinary instead of the local filesystem.  
- Images are served via CDN for fast performance.  
- Transformations (resize, crop, optimize) ensure responsive display.  
- API keys are stored securely as environment variables.  

---

## 🚀 Deployment (Heroku + Git)
- **Version Control**  
  The project is tracked with Git. Features are developed in branches and merged into `main`.

- **Heroku Hosting**  
  The app is deployed on Heroku.  
  Pushing to the `main` branch triggers deployment automatically.  
  Environment variables (`SECRET_KEY`, `DEBUG=False`) are stored in Heroku config.

- **Database**  
  PostgreSQL is used both locally for development and in production.

---

 
## 🪞 Reflection
- Building CheckPoint demonstrated the importance of **CRUD fundamentals** in web apps.  
- Using **Heroku + Git** simplified deployment and version control.  
- Integrating **Cloudinary** made handling user images scalable and production‑ready.  
- Future improvements could include comments, categories, and search functionality.  

