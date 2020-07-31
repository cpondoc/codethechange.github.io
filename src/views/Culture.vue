<template>
  <div class="container-fluid">
    <div class="intro">
      <h1 id="hook">Culture at CtC</h1>
      <p class = 'hook-sub'>
        Code the Change is about more than just technical work—we strive continuously to incorporate our core values in our club culture.
      </p>
    </div>
    <div id="white">
      <div id="content">
        <!-- Line breaks in the markdown are treated literally -->
        <VueShowdown markdown="
# Our Values
We commit to upholding the letter and spirit of these values both as individuals and as a community. We hold each other and ourselves accountable for ensuring everything we do at Code the Change represents these values.

## Growth

- We learn from each other and our partners, and we enable others’ learning by sharing our skills, knowledge, and perspectives.
- We support each other's growth by making space for each other, and embracing our own and each other’s mistakes as opportunities for growth.
- We give constructive feedback kindly and receive it graciously.
- We take time to reflect and improve.

## Community

- We respect, value, support, and cherish each other.
- We welcome members of all backgrounds and abilities, regardless of age, body size, visible or invisible disability, ethnicity, sex characteristics, gender identity and expression, level of experience, education, socio-economic status, nationality, personal appearance, race, religion, or sexual identity and orientation (The Contributor Covenant). We have no tolerance for discrimination on the basis of these characteristics, and we accept the responsibility to prevent harassment, abuse, and intimidation of any kind within our organization.
- We cultivate empathy and kindness for each other, our partners, and the broader community.
- We are honest and forthright with each other, our partners, and all others with whom we interact. We strive to operate transparently wherever possible.

## Humility

- We forge reciprocal relationships with our partners. We help and learn from each other in a bilateral exchange, not a unilateral movement of aid from us to them.
- We are fallible, and in fact we will surely make mistakes. We create a space with safeguards and a culture that makes those mistakes okay.
- We recognize that we need each other’s help, so we ask for help and encourage each other to do likewise.

## Positive Impact

- We commit to ensuring our work has a positive impact for people who need it.
- We are mindful of the impact our work has, and we accept responsibility for that impact, both good and bad.

## Accountability

- Our partners rely on us, and we rely on each other. Therefore, we accept the responsibility to deliver what we promise.
- We hold ourselves accountable to each other, our partners, and our community for the impacts of our choices.
- We clearly communicate our expectations and capabilities to each other and our partners.

## Self-Care

- We understand that we cannot effectively work with our partners unless we also care for each other and ourselves.
- We make time to care for each other.
- We recognize that we all need to practice self-care, so we encourage and support each other in practicing it.

# Addressing Failures and Improving our Culture

We are always striving to improve our culture, and suggestions from you about how we can improve or areas where we are failing are important to us. Similarly, we want to hear about any concerns you have regarding actions or situations that contravene the spirit of these values. Please direct these suggestions and concerns to any of the following:
- Club Leadership: Contact information at https://codethechange.stanford.edu
- The Haas Center: haascenter@stanford.edu
- Stanford’s Office of Community Standards: community-standards@stanford.edu

If you report to club leadership, we promise that we will do the following:
- We will keep your report confidential. We may have to share your report to address your concerns, for example with other members of club leadership to decide how to respond, with Stanford University, or with law enforcement, but we value your privacy and will work to protect it.
- We will work swiftly to address any failings or areas of improvement you report to us.
- If you like, we will include you as much as possible in our work to respond to your report. In some cases we may not be able to share the details of our response with you, but we will share what we can.

For example, if you are concerned that one of our projects may harm someone, please let us know. Such a harm runs contrary to our *Positive Impact* value, and we will take corrective action. Similarly, we don’t want anyone to feel excluded from our community, as exclusion runs contrary to our *Community* value, so we work to make our community welcoming for everyone. If you have a suggestion for how we can do so better, we would love to hear it!
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
