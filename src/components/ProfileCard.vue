<template>
    <div>
        <figure class="tint" :style="{ '--gradient': colors['tint-'+color]}">
            <img id="profile-photo" :src="imageSrc"/>
            <div class="links">
                <a :href="social.link" :key="social.link" class="hvr-glow link-button" v-for="social in socials" :style="{ 'background-color': colors['bold-'+color]}">
                    <img class="social-icon" :src="social.image" />
                </a>
            </div>
        </figure>
        <p id="name">{{ name }}</p>
        <p id="position"> {{ position.toUpperCase() }} </p>
    </div>
</template>
<script>
import github from '@/assets/img/github-icon.png'
import email from '@/assets/img/email.png'
import linkedin from '@/assets/img/linkedin-icon.png'
import colors from '@/data/colors.json'

export default {
  name: 'profileCard',
  props: ['imageSrc', 'name', 'position', 'links', 'color'],
  data: function () {
    let socials = []
    for (let link in this.links) {
      let image = ''
      if (link === 'github') {
        image = github
      } else if (link === 'linkedin') {
        image = linkedin
      } else if (link === 'email') {
        image = email
        if (!this.links[link].startsWith('mailto:')) {
          this.links[link] = 'mailto:' + this.links[link]
        }
      }
      socials.push({ link: this.links[link], image: image })
    }
    return {
      socials: socials,
      colors: colors
    }
  },
  mounted () {
    const css = 'table td:hover{ background-color: #00ff00 }'
    const style = document.createElement('style')
    if (style.styleSheet) {
      style.styleSheet.cssText = css
    } else {
      style.appendChild(document.createTextNode(css))
    }
    document.getElementsByTagName('head')[0].appendChild(style)
  }
}
</script>
<style scoped lang="scss">

@import '../theme.scss';

/* Glow FROM HOVER.CSS */
.hvr-glow {
  display: inline-block;
  vertical-align: middle;
  -webkit-transform: perspective(1px) translateZ(0);
  transform: perspective(1px) translateZ(0);
  box-shadow: 0 0 1px rgba(0, 0, 0, 0);
  -webkit-transition-duration: 0.3s;
  transition-duration: 0.3s;
  -webkit-transition-property: box-shadow;
  transition-property: box-shadow;
}

.hvr-glow:hover, .hvr-glow:focus, .hvr-glow:active {
  box-shadow: 0 0 8px rgba(0, 0, 0, 0.6);
}

$icon-size: 30px;

.links{
    transition: all 0.5s ease;
    position: absolute;
    top: 80px;
    width: 100%;
    left: 0;
    justify-content: space-around;
}

.tint > .links  { display:none; }
.tint:hover > .links { display:flex; }

.tint:hover{
  --gradient: black;
  &::before {
    content: "";
    width: 200px;
    height: 200px;
    display: block;
    position: absolute;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    transition: all .3s linear;
    background: var(--gradient);
  }
}

.social-icon {
  width: $icon-size;
  height: $icon-size;
}

.link-button {
  padding: 10px;
}

.tint {
  float: left;
  width: 200px;
  height: 200px;
  border-radius: 8px;
  position:relative;
}

#profile-photo {
  width: 200px;
  height: 200px;
}

#name {
  font-family: 'Open Sans';
  font-size: 15px;
  font-weight: 600;
  font-style: normal;
  font-stretch: normal;
  line-height: normal;
  letter-spacing: normal;
  text-align: left;
  color: #545454;
  margin-bottom: 10px;
}

#position {
  font-family: 'Open Sans';
  font-size: 10px;
  font-weight: 800;
  font-style: normal;
  font-stretch: normal;
  line-height: normal;
  letter-spacing: normal;
  text-align: left;
  color: #545454;
}

</style>
