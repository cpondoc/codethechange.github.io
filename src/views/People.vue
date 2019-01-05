<template>
  <div id="about-content">
    <div id="header-text-content" class="row">
      <div class="col-12">
        <h1 id="margins">We’re a supportive team that emphasizes growth above all.</h1>
      </div>
    </div>
    <div class="row  white-bg">
      <h1 class="title" style="color: #ffaf40">Leadership</h1>
    </div>
    <div class="profile-container row white-bg">
        <profile-card id="card" v-for="person in leadership" :key="person.name" :name="person.name" :imageSrc="person.imageSrc" :position="person.role" />
    </div>
    <div v-for="team in projectTeams" :key="team.name">
      <div class="row white-bg">
        <h3 class="project-team">PROJECT TEAM:</h3>
      </div>
    </div>
  </div>
</template>
<script>
import ProfileCard from '@/components/ProfileCard.vue'
import people from '@/data/people.json'
import projects from '@/data/projects.json'

export default {
  name: 'people',
  components: { ProfileCard },
  data () {
    const projectTeams = []
    for (let project of projects) {
      if (project.wip) {
        projectTeams.push(project)
      }
    }
    return {
      leadership: [ people['drew'], people['yuguan'], people['han'] ],
      projectTeams: projectTeams
    }
  }
}
</script>
<style scoped lang="scss">
@import '../theme.scss';

.project-team {
  font-family: 'Open Sans';
  font-size: 10px;
  font-weight: 800;
  font-style: normal;
  font-stretch: normal;
  line-height: normal;
  letter-spacing: 0.2px;
  color: $bold-purple !important;
}

#card {
  margin-left:75px;
}

.profile-container {
  display:flex;
}

#header-text-content {
  background-color: #262626;
  font-family: Comfortaa;
  font-size: 72px;
  font-weight: bold;
  font-style: normal;
  font-stretch: normal;
  line-height: 1.42;
  letter-spacing: normal;
  color: #ffffff;
}

.white-bg {
  background-color: #ffffff;
}

.title {
  margin-top: 30px;
  margin-left: 75px;
  font-family: Comfortaa;
  font-size: 48px;
  font-weight: bold;
  font-style: normal;
  font-stretch: normal;
  line-height: normal;
  letter-spacing: normal;
  text-align: center;
  color: #ffb44b;
  display:block;
}

.row {
  margin: 0;
}

#margins {
  max-width: 600px;
  margin: 40px;
}
</style>
