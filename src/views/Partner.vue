<template>
  <div class="container">
    <div class="row">
      <div class="col-12">
        <h1 id="hook"> Talk to us about building impactful software together.</h1>
      </div>
    </div>
    <br />
    <br />
    <div class="row">
      <div class="col-7" id="form">
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
          <div class="form-group row">
            <label for="name" class="col-4 col-form-label">Your name</label>
            <div class="col-8">
              <input type="text" v-model="name" class="form-control input" name="name" placeholder="John Smith">
            </div>
          </div>
          <div class="form-group row">
            <label for="email" class="col-4 col-form-label">Your email</label>
            <div class="col-8">
              <input type="text" v-model="email" class="form-control input" name="email" placeholder="name@example.com">
            </div>
          </div>
          <div class="form-group row">
            <label for="name" class="col-4 col-form-label">Organization site</label>
            <div class="col-8">
              <input type="text" v-model="site" class="form-control input" name="site" placeholder="https://yoururl.com">
            </div>
          </div>
          <div class="form-group row">
            <label for="name" class="col-4 col-form-label">Proposal upload</label>
            <div class="col-4">
              <label class="btn upload-button">
                {{ filename }} <input type="file" @change="fileUpload" name="proposal" style="display: none;">
              </label>
            </div>
            <div class="col-4" id="optional">
              *Optional
            </div>
          </div>
          <div class="form-group row">
            <label for="name" class="col-4 col-form-label">Project summary</label>
            <div class="col-8">
              <textarea id="summary-text" v-model="summary" class="form-control input" name="summary" placeholder="Describe the project here." cols="40" rows="7"></textarea>
            </div>
          </div>
          <div class="form-group row">
            <div class="col-9"></div>
            <div class="col-3">
              <button type="submit" @click="onSubmit" id="submit" class="btn btn-default">SUBMIT</button>
            </div>
          </div>
        </form>
      </div>
      <div class="col-5">
        <div class="row">
          <div class="header col-12">Eligibility</div>
        </div>
        <div class="row">
          <div class="col-12 paragraph">
            You must be a nonprofit or low-resourced social venture that
            needs volunteer support for an impactful computer science
            project. For details on how we evaluate projects, see our
            <router-link class="small-link-text" to="/partner_criteria">
              partner criteria
            </router-link>.
          </div>
        </div>
        <br />
        <br />
        <div class="row">
          <div class="header col-12">What we offer</div>
        </div>
        <div class="row">
          <div class="col-12 paragraph">
            Technical leadership and support from Stanford student volunteers dedicating 5 to 10 hours per week on the project free of cost.
          </div>
        </div>
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
      alert('hi')
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
          console.log(res)
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
            this.finishedTitle = 'Form Submission Error. '
            this.finishedMessage = 'Unfortunately, we\'ve encountered some server error. Please email drewgreg [at] stanford [dot] edu with your form contents.'
          }
        })
    }
  },
  name: 'Partner',
  components: { }
}
</script>

<style lang="scss" scoped>
@import '../theme.scss';
.header {
    width: 373px;
    padding-left: 8vw;

  font-family: Comfortaa;
  font-size: 28px;
  font-weight: bold;
  font-style: normal;
  font-stretch: normal;
  line-height: 1.06;
  letter-spacing: normal;
  color: #ffffff;

}

.container{
 margin-top: 10vh;
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

.upload-button, input[type=file] {
  width: 100%;
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

.form-group {
  line-height: 45px;
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
  text-align: center
}

label#col-form-label {
  width: 197px;
  font-family: Comfortaa;
  font-size: 15px;
  font-weight: bold;
  font-style: normal;
  font-stretch: normal;
  line-height: 1;
  letter-spacing: normal;
  text-align: center;
  color: #ffffff;
}

input[type="text"]:focus, textarea:focus {
  color: $text-color !important;
  border-color: $text-color !important;
  box-shadow: 0 0 10px $text-color !important;
  background-color: rgba(0,0,0,0) !important;
}

#form {
  border-radius: 8px;
  padding: 40px;
  box-shadow: 0 4px 25px 0 rgba(41, 41, 41, 0.5);
  background-color: #292929;
}

#optional {
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
  height: 38px;
  font-family: Comfortaa;
  font-size: 36px;
  font-weight: bold;
  font-style: normal;
  text-align: center;
  font-stretch: normal;
  line-height: 1.06;
  letter-spacing: normal;
  color: #ffffff;
}

.paragraph {
  font-family: 'Open Sans';
  font-size: 21px;
    padding-left: 8vw;

  font-weight: normal;
  font-style: normal;
  font-stretch: normal;
  line-height: 1.75;
  letter-spacing: normal;
  color: #919191;
  text-align: left;
  padding-right: 100px;
}
</style>
