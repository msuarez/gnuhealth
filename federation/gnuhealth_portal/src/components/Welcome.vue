<template>
  <div class="home">
  
  <div class="banner-home">
  <div class="container text-center">
    <h1>{{ msg }}</h1>
    <img alt="GNU Health Federation" src="../assets/banner-home.png" class="u-max-full-width">
    </div>
  </div>
<div class="container text-center">
  <div class="row">
  <div class="six columns">
    <p><strong>GNU Health Documentation:</strong><br/>
    <a href="https://en.wikibooks.org/wiki/GNU_Health" target="_blank" rel="noopener"> Check out the GNU Health documentation project</a></p>
  </div>	
  <div class="six columns">
  <p><strong>Community Resources:</strong><br/>
  <a href="http://www.gnuhealth.org" target="_blank" rel="noopener">GNU Health</a> | <a href="https://twitter.com/gnuhealth" target="_blank" rel="noopener">Follow us on Twitter</a></p>
  </div>
  </div>
</div>
  </div>
</template>

<script>

export default {
  name: 'Welcome',
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

a {
  color: #42b983;
}

.banner-home {
    background-color: #00acc6;
    padding-top: 25px;
    padding-bottom: 50px;
    margin-bottom: 50px;
}
div.banner-home h1 {
    color:#ffffff;
}


div.home a {
    color: #007191;
}
</style>
