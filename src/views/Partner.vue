<template>
  <div class="container">
    <h1 id="hook"> Talk to us about building impactful software together.</h1>
    <div class="" id="form">
      <div v-if="submitted" class="row">
        <div class="col-12">
          <h1> {{ finishedTitle }} </h1>
        </div>
      </div>
      <div v-if="submitted" class="row">
        <div class="col-12">
          <h4> {{ finishedMessage }} </h4>
        </div>
      </div>
      <div v-if="submitted" class="row">
        <div class="col-12">
          <button id="submit" @click="submitted = false" class="btn btn-default"> RETRY </button>
        </div>
      </div>
      <form v-if="!submitted" @submit.prevent="onSubmit" enctype="multipart/form-data">
        <div class="form-group">
          <label for="name" class="col-form-label">Your name</label>
          <div class="col-form-input">
            <input type="text" v-model="name" class="form-control input" name="name" placeholder="John Smith">
          </div>
        </div>
        <div class="form-group">
          <label for="email" class="col-form-label">Your email</label>
          <div class="col-form-input">
            <input type="text" v-model="email" class="form-control input" name="email" placeholder="name@example.com">
          </div>
        </div>
        <div class="form-group">
          <label for="name" class="col-form-label">Organization site</label>
          <div class="col-form-input">
            <input type="text" v-model="site" class="form-control input" name="site" placeholder="https://yoururl.com">
          </div>
        </div>
        <div class="form-group">
          <label for="name" class="col-form-label">Proposal upload</label>
          <div class="col-form-input proposal-upload-row">
            <label class="btn upload-button">
              {{ filename }} <input type="file" @change="fileUpload" name="proposal" style="display: none;">
            </label>
            <div class="" id="optional">
              *Optional
            </div>
          </div>
        </div>
        <div class="form-group">
          <label for="name" class="col-form-label">Project summary</label>
          <div class="col-form-input">
            <textarea id="summary-text" v-model="summary" class="form-control input" name="summary" placeholder="Describe the project here." cols="40" rows="7"></textarea>
          </div>
        </div>
        <div class="form-group">
          <div class="">
            <button type="submit" @click="onSubmit" id="submit" class="btn btn-default">SUBMIT</button>
          </div>
        </div>
      </form>
    </div>

    <div class="eligibility">
      <div class="header">Eligibility</div>
      <div class="paragraph">
        You must be a nonprofit or low-resourced social venture that
        needs volunteer support for an impactful computer science
        project. For details on how we evaluate projects, see our
        <router-link class="small-link-text color-change"
                     to="/partner_criteria">
          partner criteria
        </router-link>.
      </div>
    </div>

    <div class="what-we-offer">
      <div class="header">What we offer</div>
      <div class="paragraph">
        Technical leadership and support from Stanford student volunteers dedicating 5 to 10 hours per week on the project free of cost.
      </div>
    </div>

  </div>
</template>

<script>
import axios from 'axios'

export default {
  data: function () {
    return {
      filename: 'ADD FILE',
      file: null,
      name: null,
      summary: null,
      email: null,
      site: null,
      submitting: false,
      submitted: false,
      finishedMessage: ''
    }
  },
  methods: {
    fileUpload (event) {
      if (event.target.files.length === 1) {
        const name = event.target.files[0].name
        this.filename = name.substr(0, 15) + (name.length > 15 ? '... ' : '')
        this.file = event.target.files[0]
      } else {
        this.filename = 'ADD FILE'
        this.file = null
      }
    },
    onSubmit () {
      if (!this.submitting) {
        this.submitting = true
        const formData = new FormData()
        if (this.file) {
          formData.append('proposal', this.file, this.filename)
        }
        formData.append('name', this.name)
        formData.append('email', this.email)
        formData.append('summary', this.summary)
        formData.append('site', this.site)
        axios.post('https://guarded-ravine-42139.herokuapp.com/partner-form', formData)
          .then(res => {
            this.submitted = true
            this.submitting = false
            if (res.error) {
              this.finishedTitle = 'Form Submission Error. '
              this.finishedMessage = 'Unfortunately, we\'ve encountered some server error. Please email drewgreg [at] stanford [dot] edu with your form contents.'
            } else {
              this.finishedTitle = 'Form Submitted!'
              this.finishedMessage = 'Thank you for reaching out. We will get back to you if we think your project is a good fit.'
            }
          })
          .error(err => {
            if (err) {
              this.submitted = true
              this.submitting = false
              this.finishedTitle = 'Form Submission Error. '
              this.finishedMessage = 'Unfortunately, we\'ve encountered some server error. Please email drewgreg [at] stanford [dot] edu with your form contents.'
            }
          })
      }
    }
  },
  name: 'Partner',
  components: { }
}
</script>

<style lang="scss" scoped>
@import '../theme.scss';

.color-change {
  color: #ffffff;
  &:hover {
    text-decoration: inherit;
    color: $accent-light;
  }
}

.container {
  margin-top: 10vh;
  display: grid;
  grid-template-columns: 1fr 1fr;
  grid-template-areas:
    "hook hook"
    "form eligibility"
    "form what-we-offer";

  @media only screen and (max-width: 700px) {
    grid-template-columns: 1fr;
    grid-template-areas:
      "hook"
      "eligibility"
      "what-we-offer"
      "form";
  }
}

.eligibility {
  grid-area: eligibility;
  padding-bottom: 10%;
}

.what-we-offer {
  grid-area: what-we-offer;
  padding-bottom: 10%;
}

#summary-text {
  text-align: left !important;
}

#submit {
  font-family: 'Open Sans';
  font-size: 20px;
  font-weight: bold;
  font-style: normal;
  font-stretch: normal;
  line-height: 2.5;
  width: 100%;
  letter-spacing: normal;
  text-align: center;
  color: #575757;
  border-radius: 8px;
  background-color: $take-action;
}

.form-group {
  display: flex;
  flex-flow: row wrap;
  justify-content: left;
  line-height: 45px;
}

.col-form-label {
  box-sizing: border-box;
  padding-right: 50px;
  padding-bottom: 30px;
  width: 200px;
  font-family: Comfortaa;
  font-size: 15px;
  font-weight: bold;
  font-style: normal;
  font-stretch: normal;
  line-height: 1;
  letter-spacing: normal;
  text-align: left;
  color: #ffffff;
  display: inline-block;
}

.col-form-input {
  flex: 1 200px;
}

input[type="text"], textarea, .form-control {
  background-color: rgba(0,0,0,0) !important;;
  color: $text-color !important;;
  outline: none !important;;
  font-size: 15px !important;;
  font-weight: normal !important;;
  font-style: normal !important;;
  font-stretch: normal !important;;
  line-height: 1 !important;;
  letter-spacing: normal !important;;
  text-align: center;
}

input[type="text"]:focus, textarea:focus {
  color: $text-color !important;
  border-color: $text-color !important;
  box-shadow: 0 0 10px $text-color !important;
  background-color: rgba(0,0,0,0) !important;
}

#form {
  grid-area: form;
  border-radius: 8px;
  padding: 40px;
  box-shadow: 0 4px 25px 0 rgba(41, 41, 41, 0.5);
  background-color: #292929;
}

.proposal-upload-row {
  display: flex;
}

.upload-button, input[type=file] {
  flex: 1 100px;
  height: 38px;
  text-align: right;
  filter: alpha(opacity=0);
  border-radius: 8px;
  background-color: #3a3a3a;
  font-family: 'Open Sans';
  font-size: 16px;
  font-weight: bold;
  font-style: normal;
  font-stretch: normal;
  letter-spacing: normal;
  text-align: center;
  color: #ffffff;
}

#optional {
  flex: 1 80px;
  font-family: 'Open Sans';
  height: 45px;
  font-size: 16px;
  font-weight: bold;
  font-style: normal;
  font-stretch: normal;
  letter-spacing: normal;
  text-align: center;
  color: #c8c8c8;
}

#hook {
  grid-area: hook;
  font-family: Comfortaa;
  font-size: 36px;
  font-weight: bold;
  font-style: normal;
  text-align: center;
  font-stretch: normal;
  line-height: 1.06;
  letter-spacing: normal;
  color: #ffffff;
  padding-bottom: 10%;
  @media only screen and (max-width: 700px) {
    padding-left: 2vw;
    padding-right: 2vw;
    font-size: 24px;
    line-height: 50px;
  }
}

.paragraph {
  font-family: 'Open Sans';
  font-size: 21px;
  padding-left: 8vw;
  padding-right: 8vw;

  font-weight: normal;
  font-style: normal;
  font-stretch: normal;
  line-height: 1.75;
  letter-spacing: normal;
  color: #919191;
  text-align: left;
  @media only screen and (max-width: 700px) {
    padding-left: 2vw;
    padding-right: 2vw;
    text-align: center;
    font-size: 21px;
    line-height: 45px;
  }
}

.header {
  padding-left: 8vw;
  padding-right: 8vw;

  font-family: Comfortaa;
  font-size: 28px;
  font-weight: bold;
  font-style: normal;
  font-stretch: normal;
  line-height: 1.06;
  letter-spacing: normal;
  color: #ffffff;
  @media only screen and (max-width: 700px) {
    padding-bottom: 5vw;
    text-align: center;
    font-size: 21px;
    line-height: 38px;
  }
}
</style>
