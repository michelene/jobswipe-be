# jobswipe - Project Proposal

## Overview

Jobswipe is an application which helps job seekers view, save, and apply for jobs which
match their search criteria.

Users must create an account and sign in in order to save personalized job lists.

Job listings are imported from https://jobs.github.com/ according to search criteria (keyword, location, fulltime) provided by the user.

For each job listing, the user can opt to save or discard the listing.

The user can review their saved jobs at any time.

## Models

- `JobSeeker`

  - `Username`
  - I plan to use Social Auth as well as Django built-in auth, so whatever is needed to support those
  - `NewJobs` # Jobs they have not yet reviewed
  - `SavedJobs` # Jobs they have specifically saved
  - Once I get everything working, I might add the feature of the JobSeeker being able to have multiple saved lists (e.g. 'Django Jobs', 'React Jobs', etc.)

- `JobPosting`

  - `GHJ ID` (The unique ID assigned by GitHub Jobs)
  - Possibly store as a [JSONField](https://docs.djangoproject.com/en/3.0/ref/contrib/postgres/fields/#jsonfield) <-- Jen, do you have any thoughts on this?

- `UnreviewedJobs`
  - `ListTitle`
  - I am not sure if I will need this as its own object. It would basically be a many-to-one (`ForeignKey`) collection of JobPostings
  - If I create this model, then `JobSeeker.NewJobs` and `JobSeeker.SavedJobs` will be of type `UnreviewedJobs`

## Technologies

- ReactJS + Material UI for front end
- Django/PostgreSQL for back end
- Django REST Framework

## 3rd Party APIs

- [GitHub Jobs API](https://jobs.github.com/api)

## Django Components

- psycopg2-binary
- django-extensions
- cors-headers
- djangorestframework
- markdown
- django-filter

## Material UI Components

- [Signup Template](https://github.com/mui-org/material-ui/tree/master/docs/src/pages/getting-started/templates/sign-up)

## MVP

- Signup (Account creation and deletion capability)
- Responsive design (Hamburger Menu)
- Incorporate Material UI's swipe feature, in addition to Save/Discard buttons
- Ability to apply for the job directly from the app
- Job listing should display company logo and render HTML formatting
- Deployed to Heroku

## Silver, Gold, Platinum (Post-MVP)

- Social login
- Create an iOS app using React Native
- Allow a user to curate multiple lists e.g. 'Applied To'

## Questions

- How to model data
- I have created routes for PostgreSQL/Django User/Group. Do I need a separate model for JobSeeker, or can I piggyback off of User? (I suspect I need to create a separate JobSeeker model.)

## User Stories

## Links

- [Front End Repo](https://github.com/michelene/jobswipe_fe)
- [Back End Repo](https://github.com/michelene/jobswipe-be)
- [Deployed Front End]()
- [Deployed Back End]()
