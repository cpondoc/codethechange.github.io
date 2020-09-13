<template>
  <div class="container-fluid">
    <div class="intro">
      <h1 id="hook">Ways to Contribute</h1>
      <p class = 'hook-sub'>
        Want to help with our projects? We want to support you whether
        you can contribute an hour a week or ten.
      </p>
    </div>
    <div id="white">
      <div id="content">
        <!-- Line breaks in the markdown are treated literally -->
        <VueShowdown markdown="
# Contribute Independently

We welcome independent contributions, whether you are exploring a project through starter issues or have too tight a schedule to contribute regularly. There are no pre-requisites for this kind of contribution.

If you run into problems, please reach out to the team whose project you are working on via email or Slack. If a team has a dedicated Slack channel for new members, e.g. `#oppia-new`, that's a great place to ask.

Your contributions will be credited to you in the project's normal manner (e.g. public GitHub commits, an `AUTHORS` file, etc.).

# Join a Team

If you're ready to commit more time to a project you're interested in, consider joining as a member! First, we ask that you complete 2 starter tasks and have your changes accepted by the partner organization. From then on, we expect you to be engaged with the project via contributions, email, attending meetings, Slack, etc. weekly. If we don't see any engagement for 14 days without explanation, we may remove you.

As a member of the team, your team's Slack channel is a great place to ask questions and stay up-to-date with your teammates work. Team meetings are also great ways to get help, as is/are your team lead(s).

If you like, we'll add your photo and contact information to our website to showcase your contributions. As a member, you are considered an official member of the VSO, so we'll add you on OrgSync. Your contributions will also be credited to you in the project's normal manner, and your increased contributions may earn you further recognition from the partner, e.g. joining their GitHub organization.

# Lead a Team

Good team leads are indispensible to the success of our projects. If you're interested in helping in this way, please reach out to the club leadership!

# Lead the Club

If you are interested in being a club officer, let us know! We hold elections each spring. Our officers select team leads and support teams by acquiring funding, finding partners, marketing projects, and much more.
        "/>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
@import '../theme.scss';

.container-fluid {
  padding: 0;
}

.intro {
  padding: 50px 50px 50px 250px;
  @media only screen and (max-width: 700px) {
    padding: 20px;
  }
}

#white {
    background-color: #ffffff;
    display: flex;
    justify-content: center;
}

#content {
    padding: 60px;
    max-width: 900px;
    color: #5e5e5e;
    font-family: 'Comfortaa';
    font-size: 1em;
    font-style: normal;
    font-stretch: normal;
}

#hook{
  font-size: 5em;
}

.hook-sub{
  font-size: 1.2em;
  padding-top: 2.5vh;
}
</style>
