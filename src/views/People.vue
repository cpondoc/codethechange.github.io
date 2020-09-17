<template>
  <div id="about-content">
    <h3 id="margins">We’re a supportive team that emphasizes growth above all.</h3>
    <div class="row white-bg">
      <h1 class="margin-top title" style="color: #ffaf40">Leadership</h1>
    </div>
    <div class="profile-container row white-bg">
      <profile-card id="card" :color="'orange'" v-for="person in leadership" :key="person.name" :name="person.name" :imageSrc="person.imageSrc" :position="person.role" :links="person.links" />
    </div>
    <div v-for="team in projectTeams" :key="team.name" class="white-bg">
      <div class="row">
        <h3 class="margin-top project-team" :style="{ color: colors['bold-' + team.color] }">PROJECT TEAM:</h3>
      </div>
      <div class="row">
        <h1 class="title" :style="{ color: colors['bold-' + team.color] }">{{ team.name }}</h1>
      </div>
      <div class="profile-container row">
        <profile-card id="card" v-for="person in team.people" :color="team.color" :key="person.name" :name="person.name" :imageSrc="person.imageSrc" :position="person.role" :links="person.links" />
      </div>
    </div>
  </div>
</template>
<script>
import ProfileCard from '@/components/ProfileCard.vue'
import people from '@/data/people.json'
import projects from '@/data/projects.json'
import colors from '@/data/colors.json'

export default {
  name: 'people',
  components: { ProfileCard },
  data () {
    const selColors = ['purple', 'blue', 'orange']
    let i = 0
    const projectTeams = []
    for (let project of projects) {
      if (project.wip && project.team.length > 0) {
        let teamPeople = []
        for (let person of project.team) {
          teamPeople.push(people[person])
        }
        project.people = teamPeople
        project.color = selColors[i++ % selColors.length]
        projectTeams.push(project)
      }
    }
    let leadership = []
    for (let person in people) {
      if (people[person].leadership) {
        leadership.push(people[person])
      }
    }
    return {
      leadership: leadership,
      projectTeams: projectTeams,
      colors: colors
    }
  }
}
</script>
<style scoped lang="scss">
@import '../theme.scss';
$people-left-margin: 75px;

.margin-top{
  margin-top: 75px;
}

.project-team {
  margin-left: $people-left-margin;
  font-family: 'Open Sans';
  font-size: 10px;
  font-weight: 800;
  font-style: normal;
  font-stretch: normal;
  line-height: normal;
  letter-spacing: 0.2px;
}

#card {
  margin-left: $people-left-margin;
}

.profile-container {
  display:flex;
}

#header-text-content {
  background-color: #262626;
  font-family: Comfortaa;
  font-size: 72px;
  font-weight: bold;
  line-height: 1.42;
  color: #ffffff;
}

.white-bg {
  background-color: #ffffff;
}

.title {
  margin-left: $people-left-margin;
  font-family: Comfortaa;
  font-size: 3em;
  font-weight: bold;
  text-align: center;
  color: #ffb44b;
  margin-bottom: 5vh;
  @media only screen and (max-width: 700px) {
    font-size: 2em;
  }
}

.row {
  margin: 0;
}

#margins {
  max-width: 650px;
  margin: 60px;
  margin-top: 15vh;
  margin-bottom: 15vh;
  font-size: 2.5em;
  text-align: left;
  line-height: 1.42;
}
</style>
