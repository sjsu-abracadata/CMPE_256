<template>
  <div class="hello">
    <nav class="navbar navbar-dark bg-dark">
      <span style="color:white; vertical-align:center;"><h4>{{msg}}</h4></span>
      
    </nav>
    <div class="card">
        <div class="card-header">
            <div class="row align-items-center">
                <div class="col">                      
                    <h4 class="card-title">Icon Circle Buttons Examples</h4>  
                    <p class="text-muted mb-0">A button variant for using only icons.Add <code>.btn-icon-circle</code></p>                    
                </div><!--end col-->                                                                             
            </div>  <!--end row-->                                  
        </div><!--end card-header-->
        <div class="card-body">    
            <div class="button-items"> 
                <button type="button" class="btn btn-outline-info btn-icon-circle btn-icon-circle-sm"><i class="fab fa-skype"></i></button>
                <button type="button" class="btn btn-outline-danger btn-icon-circle btn-icon-circle-sm"><i class="fab fa-pinterest"></i></button>
                <button type="button" class="btn btn-outline-dark btn-icon-circle btn-icon-circle-sm"><i class="fab fa-github"></i></button>  
            </div>
        </div><!--end card-body-->                                
    </div><!--end card-->
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
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
