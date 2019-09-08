<template>
    <div id="profile-page">
        <div id="error404" v-if="!project">
            <h1>404 Error</h1>
            <p>We're sorry, but the <b>{{ this.$route.query.name }}</b> project could not be found.</p>
        </div>
        <div v-else>
            <div id="header-text-content">
                <h1 id="margins">{{ project.summary }}</h1>
            </div>
            <div id="white">
                <div id="content">
                    <i>{{ project.organization }}</i>
                    <br />
                    <br />
                    <div id="card">
                        <img v-if="project.background" :src="project.background" />
                        <p v-for="bullet in project.bullets" :key="bullet">{{ bullet }}</p>
                    </div>
                    <br />
                    <br />
                    <h1 id="overview">Project Overview</h1>
                    <div id="narrative" v-html="project.narrative"></div>
                    <div v-for="asset in project.assets" :key="asset.src" class="asset">
                        <img :src="asset.src"/>
                        <p class="caption"> {{asset.caption}} </p>
                    </div>
                    <div>
                        <h2 id="cool">Think this is cool? Get involved.</h2>
                        <div id="button-container">
                            <div class="involve-button">
                                <p>STUDENTS</p>
                                <router-link to="/join" ><button class="btn">JOIN</button></router-link>
                            </div>
                            <div class="involve-button">
                                <p>ORGANIZATIONS</p>
                                <router-link to="/partner"><button class="btn">PARTNER</button></router-link>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import projects from '@/data/projects.json'
export default {
  name: 'profile',
  data () {
    for (let project of projects) {
      if (project.name === this.$route.query.name) {
        return {
          project: project
        }
      }
    }
    return {}
  }
}
</script>
<style lang="scss" scoped>
@import '../theme.scss';

.involve-button {
    font-weight: 800;
    p {
        color: #414141;
        font-size: 1.2em;
        text-align: center;
    }
    button {
        width: 237px;
        height: 85px;
        border-radius: 8px;
        box-shadow: 0 4px 25px 0 rgba(50, 114, 100, 0.5);
        background-color: $accent-medium;
        font-weight: 800;
        color: #ffffff;
    }
}

#button-container {
    display: flex;
    flex-flow: row wrap;
    justify-content: space-evenly;
}

#margins {
  box-sizing:border-box;
  padding: 100px;
  padding-left: 10%;
  padding-right: 10%;

}

#cool {
    font-family: Comfortaa;
    font-size: 2em;
    font-weight: bold;
    font-style: normal;
    font-stretch: normal;
    line-height: 1.43;
    letter-spacing: 0.5px;
    color: $accent-medium;
    padding-top: 5vh;
    padding-bottom: 5vh;
    text-align: center;

}

#header-text-content {
  background-color: #262626;
  font-family: Comfortaa;
  font-size: 1.5em;
  font-weight: bold;
  font-style: normal;
  font-stretch: normal;
  line-height: 1.42;
  letter-spacing: normal;
  color: #ffffff;
  text-align: center;
}

#narrative {
    a {
        color: blue;
    }
}

#error404 {
    width: 100vw;
    text-align:center;
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

#card {
  box-shadow: 0 4px 25px 0 rgba(122, 122, 122, 0.5);
  background-color: #ffffff;
  padding: 30px;
  img {
      max-width: 100px;
  }
}

#overview {
    font-family: Comfortaa;
    font-size: 20px;
    font-weight: bold;
    font-style: normal;
    font-stretch: normal;
    line-height: 2.14;
    letter-spacing: 0.4px;
    color: #323232;
}

.asset {
    padding-top: 40px;
    padding-bottom: 40px;
}

img {
    width: 100%;
}

.caption {
    text-align: center;
}
</style>
