<template>
    <div >
        <img id="profile-photo" :src="imageSrc"/>
        <br />
        <p id="name">{{ name }}</p>
        <p id="position"> {{ position.toUpperCase() }} </p>
    </div>
</template>
<script>
export default {
  name: 'profileCard',
  props: ['imageSrc', 'name', 'position']
}
</script>
<style scoped lang="scss">
@import '../theme.scss';

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

#profile-photo {
  width: 200px;
  height: 200px;
  border-radius: 8px;
}

</style>
