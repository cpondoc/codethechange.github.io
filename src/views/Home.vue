<template>
  <div class="container" id="home-content">
    <div class="row" id="intro">
      <div class="col-lg-5" id="text">
        <br />
        <h1 id="hook">Code from day one, with impact.</h1>
        <hr id="line" />
        <p id="subtitle">Welcome to a passionate club of engineers and makers.</p>
        <a href="#" v-scroll-to="{
          el: '.projects',
          duration: 500,
          easing: 'linear',
          offset: -80,
          force: true,
          cancelable: true,
          x: false,
          y: true
        }" id="view-text">View our work</a>
      </div>
      <div class="col-lg-7" id="stanford-wrapper">
        <img id="stanford" src="@/assets/img/stanford@2x.png" />
      </div>
    </div>
    <div v-for="project in caseStudies" :key="project.name" class="row projects">
      <div class="col-lg-5">
        <p class="year" :style="{ color: themeColors['light-'+project.color] }">{{ project.year }}</p>
        <p class="org-name">{{ project.name}}</p>
        <p class="summary">{{ project.summary }}</p>
        <button @click="goToProfile(project.name)" :style="{ backgroundColor: themeColors['bold-'+project.color] }" class="btn read-btn">READ</button>
      </div>
      <div class="col-lg-7 image-holder">
        <img :src="baseUrl + project.background" />
      </div>
    </div>
  </div>
</template>

<script>
import Projects from '@/data/projects.json'
import colors from '@/data/colors.json'

export default {
  name: 'home',
  data () {
    const selColors = ['blue', 'orange', 'purple']
    let i = 0
    let caseStudies = []
    for (let x of Projects) {
      if (x.featured) {
        x.color = selColors[i++ % selColors.length]
        caseStudies.push(x)
      }
    }
    return {
      caseStudies: caseStudies,
      baseUrl: process.env.BASE_URL,
      themeColors: colors
    }
  },
  methods: {
    goToProfile (name) {
      this.$router.push({ path: 'profile', query: { name: name } })
    }
  }
}
</script>

<style scoped lang="scss">
@import '../theme.scss';

.container {
  padding: 0;
  margin-left: 60px;
  margin-right: 60px;
  @media only screen and (max-width: 700px) {
    margin-left: 20px;
    margin-right: 20px;
  }
  > * {
    margin: 0;
    padding: 0;
    > * {
      padding-left: 0;
      padding-right: 0;
    }
  }
}

#intro {
  margin-top: 5em;
  margin-bottom: 4em;
  @media only screen and (max-width: 700px) {
    margin-top: 0;
    margin-bottom: 1em;
  }
  #text {
    #hook {
      font-family: Comfortaa;
      font-size: 3.6em;
      font-weight: bold;
      line-height: 9vh;
      color: white;
      width: 24vw;
      @media only screen and (max-width: 700px) {
        font-size: 2em;
        line-height: inherit;
      }
    }

    #line {
      margin-top: 3vh;
      margin-bottom: 3vh;
      width: 50%;
      height: 2px;
      background-color: $home-accent;
      margin-left: 0px;
    }

    #subtitle {
      font-family: 'Open Sans';
      font-size: 1.5em;
      color: white;
      margin-bottom: 2em;
    }

    #view-text {
      font-family: Comfortaa;
      font-size: 24px;
      font-weight: bold;
      color: $home-accent;
    }
  }

  #stanford-wrapper {
    text-align: right;
    #stanford {
      max-width: 30em;
    }
    @media only screen and (max-width: 700px) {
      text-align: center;
      #stanford {
        max-width: 10em;
      }
    }
  }
}

.projects {
  font-family: Comfortaa;
  margin-top: 6em;

  .year {
    font-size: 2em;
    font-weight: bold;
  }
  .org-name {
    font-size: 2.4em;
    font-weight: bold;
    color: white;
  }
  .summary {
    font-size: 1.4em;
    line-height: 1.5;
    color: #ffffff;
  }

  .read-btn {
    width: 25%;
    border-radius: 50px;
    box-shadow: 0 2px 10px 0 rgba(151, 33, 255, 0.5);
    background-color: $bold-purple;
    font-family: 'Open Sans';
    font-size: 1.2em;
    font-weight: 800;
    color: white;
  }

  .image-holder {
    margin-top: 10px;
    text-align: center;

    img {
      background-color: white;
      padding: 10px;
      max-width: 45%;
      border-radius: 8px;
    }

    &:before {
      content: "";
      display: block;
      position: absolute;
      top: 0;
      bottom: 0;
      left: 0;
      right: 0;
      transition: all .3s linear;
    }
  }
}
</style>
