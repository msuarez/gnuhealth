<template>
  <div class="home">
    <h1>{{ msg }}</h1>
    <p>
      Check out the GNU Health documentation project at<br>

      <a href="https://en.wikibooks.org/wiki/GNU_Health" target="_blank"
        rel="noopener">GNU Health Documentation</a>.
    </p>
    <h3>Community Resources</h3>
    <ul>
      <li><a href="http://www.gnuhealth.org" target="_blank"
        rel="noopener">GNU Health</a></li>
      <li><a href="https://twitter.com/gnuhealth" target="_blank"
        rel="noopener">Follow us on Twitter</a></li>
    </ul>
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
</style>
