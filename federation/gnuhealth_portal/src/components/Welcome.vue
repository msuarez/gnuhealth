<template>
  <div class="home">
  <div class="banner-home">
    <h1>{{ msg }}</h1>
    <img alt="GNU Health Federation" src="../assets/banner-home.png">
  </div>

  <div class="row">
  <div class="col-sm-6">
    <p><strong>GNU Health Documentation:</strong><br/>
    <a href="https://en.wikibooks.org/wiki/GNU_Health" target="_blank" rel="noopener"> Check out the GNU Health documentation project</a></p>
  </div>	
  <div class="col-sm-6">
  <p><strong>Community Resources:</strong><br/>
  <a href="http://www.gnuhealth.org" target="_blank" rel="noopener">GNU Health</a> | <a href="https://twitter.com/gnuhealth" target="_blank" rel="noopener">Follow us on Twitter</a></p>
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
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}

.banner-home {
    background-color: #00acc6;
    padding-top: 25px;
    padding-bottom: 50px;
}
div.banner-home h1 {
    color:#ffffff;
    font-size: 40px;
    font-weight: normal;
    margin-top:0px;
    letter-spacing: -1px;
}
.col-sm-6 {
    width: 50%;
    float:left;
 }
.row {
    padding-top: 40px;
    padding-bottom: 40px;
    overflow:auto;
}

div.home a {
    color: #007191;
}
</style>
