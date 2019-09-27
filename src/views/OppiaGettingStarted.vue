<template>
  <div class="container-fluid">
    <div class="intro">
      <h1 id="hook">Oppia Getting Started Guide for Coders</h1>
      <p class = 'hook-sub'>
        Welcome! Let's get you setup to contribute to Oppia.
      </p>
    </div>
    <div id="white">
      <div id="content">
        <!-- Line breaks in the markdown are treated literally -->
        <vue-markdown>
This guide is for Stanford students who want to contribute code to [Oppia](https://www.github.com/oppia/oppia) through Stanford Code the Change. If you are looking to contribute to Oppia on your own, see Oppia's [contribution guide](https://github.com/oppia/oppia/wiki). If you are interested in contributing something other than code, please reach out to our [team leadership](http://codethechange.stanford.edu/#/people).

# Help Us Get to Know You

## Get Setup with Stanford Code the Change

1. [Join!](http://codethechange.stanford.edu/#/join)
2. Once we add you to the Slack, join the `#oppia-new` channel and say hi!

## Get Setup with Oppia

1. Sign the [CLA](https://goo.gl/forms/AttNH80OV0). We know it's annoying, but the Oppia organization requires that all contributors have signed a CLA.
2. Complete the [Oppia contributor survey](https://goo.gl/forms/otv30JV3Ihv0dT3C3) to help the team at Oppia get to know you. This helps them find projects that you might be interested in.
3. Make sure you have 2-factor authentication enabled on your GitHub account. This is required by Oppia. Instructions can be found [here](https://help.github.com/articles/securing-your-account-with-two-factor-authentication-2fa/). Afterwards, you might need to [create an access token](https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/) to access your account from the command line.
4. Join the [oppia-dev@ mailing list](https://groups.google.com/forum/#!forum/oppia-dev) and the [gitter](https://gitter.im/oppia/oppia-chat). The gitter is a great place to ask questions!

# Getting Help

As you work through the steps in this guide, you'll probably run into problems or have questions. Please reach out when this happens; we want to help! Your feedback also helps us improve this guide for future contributors. Here are some ways to get help:

* Message in the `#oppia-new` slack channel
* Email the team leadership
* Ask in the Oppia gitter

# Setup Your Development Environment

1. Create a new folder to store your Oppia work. For the purposes of this guide, we'll assume you created a folder named `opensource` in your home folder (`~/opensource` where the `~` is an abbreviation for your home directory).
2. Navigate to the [Oppia GitHub repository](https://www.github.com/oppia/oppia) and click `Fork`. Sign in to your GitHub account if prompted. Once the forking is complete, go to `github.com/[yourGitHubUsername]/oppia`, where the fork operation just created a copy of the Oppia repository for you.
    * What Forking Does: When you fork the Oppia repository, you create a copy of it that you own and have full access to. Instead of changing the main Oppia repository, which you don't have access to yet, you can change your own copy and then ask (using what's called a pull request) to send those changes back to the main repository.
3. In the terminal, navigate to the `opensource` directory (folder) you created earlier. You can do this by running `cd ~/opensource`. Then get a copy of your fork of the Oppia repository like this:

   ```
   $ git clone https://github.com/[yourGitHubUsername]/oppia.git
   ```

   replacing `[yourGitHubUsername]` with your actual username. This will clone (download) your fork to `~/opensource/oppia`.
4. In the terminal navigate to the Oppia repository you cloned. You can do this by running `cd ~/opensource/oppia`. Then add the main oppia repository as a remote named `upstream` like this:

   ```
   $ git remote add upstream https://github.com/oppia/oppia.git
   ```

   This will let you update your fork with changes from the main repository.
5. Follow the installation instructions in Oppia's wiki for your platform: [Linux](https://github.com/oppia/oppia/wiki/Installing-Oppia-%28Linux%29), [macOS](https://github.com/oppia/oppia/wiki/Installing-Oppia-%28Mac-OS%29), and [Windows](https://github.com/oppia/oppia/wiki/Installing-Oppia-%28Windows%29).
    * Except for where a command in the installation instructions includes `sudo`, don't use `sudo` during the installation. It's not necessary! If you are running into permission issues, ask us for help.
    * If you run into problems, [here](https://github.com/oppia/oppia/wiki/Issues-with-installation%3F) are some troubleshooting tips.

# Get Started Learning the Technologies Oppia Uses

If you aren't familiar with the following technologies, we strongly encourage you to check out some of the listed resources to develop a basic understanding. We don't expect anyone to become an expert in these technologies before starting, but having seen the basics will help you get started. We suggest spending no more than a couple hours learning each new topic, and many will be much faster!

* Git: Git is a tool for managing many different versions of a file and the history of changes that have been made to it. It is commonly used by software developers to track different versions of their code. Our very own Drew Gregory created a tutorial to introduce you to using git, which you can find [here](https://stanford-code-the-change-guides.readthedocs.io/en/latest/guide_git.html).
* HTML: HTML is a language used across the web to style the text on webpages. Further, it often defines the basic framework within which the rest of a site is constructed. Mozilla has a [guide](https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML) you can check out.
* Javascript: Javascript implements the logic in many websites. Mozilla has a [guide](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/JavaScript_basics) you can use, but don't worry about learning much more than the very elementary here because Oppia uses AngularJS instead of using plain Javascript. However, knowing a bit of Javascript will make it much easier to learn AngularJS.
* AngularJS (v1): AngularJS is a framework that makes writing Javascript easier. We recommend the [official tutorial](https://docs.angularjs.org/tutorial/index), and Oppia also recommends [this video](https://www.youtube.com/watch?v=nO1ROKMjPqI&list=PLvZkOAgBYrsS_ugyamsNpCgLSmtIXZGiz). Oppia's frontend is written in AngularJS, and there are more projects available in the frontend than the backend. Thus, we highly recommend developing your AngularJS knowledge, even if you already know Oppia's backend languages.

Backend (python) and developer tooling (bash) projects are available, but there aren't as many. This is why we recommend learning AngularJS.

# Starter Issues

At this point, you should be able to run the Oppia site locally on your computer, and you should have a basic understanding of Git, HTML, and AngularJS. For starter issues, check out [our trello](https://trello.com/b/ScAy6Mu5/oppia). Let us know what you'd like to work on, and we'll reserve that issue for you. If nothing there strikes your fancy, take a look at the pinned issues at the top of the [Oppia issues page](https://github.com/oppia/oppia/issues).

        </vue-markdown>

      </div>
    </div>
  </div>
</template>

<script>
import VueMarkdown from 'vue-markdown'

export default {
  data: function () {
    return {}
  },
  computed: {
  },
  methods: {
  },
  name: 'OppiaGettingStarted',
  components: {
    VueMarkdown
  }
}
</script>

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
    font-family: 'Open Sans';
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
