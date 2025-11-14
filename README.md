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


## Testing

### Manual testing:

| Function | Test | Result |
|---|---|---|
| Responsive UI | In Chrome devtools, look at every page on every size of screen | Function works: Page displays correctly on all sizes. |
| Users can sign up, log in and log out | When logged out, clicked sign up, and filled out the form. When logged in, I logged out. When logged out, I logged in. | The function works: I was able to create a new account, logout, and log in. |
| Reactions, when logged in | When logged in, click each reaction on each post twice. Try clicking them when logged out. | The function works: Reactions can be made and cancelled by the logged in user. When not logged in, clicking redirects to the login page. |
| Users can delete their own posts only | When logged out, see if it is possible to delete other users' posts, or delete your own posts. When logged in, see if you can delete other users' posts, and your own. Look for a warning before deletion. See if the post has disappeared. | The function works: When logged out, no delete buttons appear on the posts. When logged in, delete button only appears on my own posts. Clicking that button gives you a warning before deletion. After deletion, that post is gone. |
| Users can edit their own posts only | When logged out, see if it is possible to edit other users' posts, or edit your own posts. When logged in, see if you can edit other users' posts, and your own. See if the post has changed as expected. | The function works: When logged out, no edit buttons appear on the posts. When logged in, edit button only appears on my own posts. Clicking that button brings you to an edit page. The changes made there were reflected in the new post. |
| User can see posts and images | Go to the site and see if all the posts and images are there. | The function works: I could see all the posts and images. |
| Signed in users can create posts | See if I can create a post when not logged in. When logged in, see if I can create a post. | When not signed in, no "create post" link appears. When logged in, "create post" link is visible. I put in a title, text and image, and on submission it appeared on the main page with the other posts. |
| All links | Click all links in the navbar and footer (checkpoint logo, home, create post, logout, sign up, follow on github) | The function works, all links went to where they should. |

### Lighthouse Testing:

![lighthouse result](/static/images/lighthouse-test-result.PNG)

### Python Linting
| File | Pass/Fail | Img |
|---|---|---|
| models | Pass | ![Alt text](/static/images/models.png) |
| views | Pass | ![Alt text](/static/images/views.png) |
| urls | Pass | ![Alt text](/static/images/urls.png) |

### Notes
- We have a small issue inside the base templates that pushes the burger menu off the navbar in the smallest screen sizes. We wanted to address this but agreed not to change any code midday Friday as to not cause any other larger issues elsewhere, we've currently deemed this an acceptable bug as the smallest screen sizes (foldables) are still quite niche tech but this will be fixed in later revisions.