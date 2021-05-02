<template>
    <div id="map-home">
        <br> <br> <br> <br> <br> <br> <br>
    
        <div class="container">
            <div class="container align-middle" id="message">
            <b-alert show variant="success">
                <h4 class="alert-heading"><strong>Welcome to Park!</strong></h4>
                <p>
                We help you provide parking spots for other people to rent or find a parking spot for yourself on any day you need!
                </p>
                <hr>
                <p class="mb-0"><strong>
                Please Register or Login above to get started
                </strong></p>
            </b-alert>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "MapHome",
}
</script>

<style scoped>
#map-home {
    background-image: url("~@/assets/parking-lot.jpg");
    background-color: black;
    height: 75vh;
    overflow-y: none;
}

#message {
    opacity: 0.9!important;
}
</style>