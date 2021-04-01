<template>
    <div id="manageSpotsOwned" class="container">
        <b-alert v-model="showError" variant="danger" dismissible>
            Failed to register spot!
        </b-alert>
        <div class="text-center">
            <p>Manage/Add Spots for Rent</p>
        </div>
        <button type="button" class="btn btn-success btn-md" v-b-modal.spot-modal>Add a New Spot for Rent</button>
        <button type="button" class="btn btn-info btn-md" style="margin-left: 15px;" @click="connectAccount()">Connect with Stripe</button>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Spot Address</th>
              <th scope="col">List Price</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="spot in spots" :key="spot.id">
              <td>{{spot.addressNum}} {{spot.street}}, {{spot.city}}, {{spot.state}} {{spot.zipcode}}</td>
              <td>${{spot.price}}/per day</td>
              <td>
                <div class="btn-group" role="group">
                  <button type="button" class="btn btn-danger btn-md">Delete Spot</button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>


        <b-modal ref="addSpotModal"
                id="spot-modal"
                title="List a New Spot for Rent"
                centered
                hide-footer>
            <b-form @submit.prevent="onSubmit" @reset="onReset" class="w-100">
                <b-form-group id="form-addressNum-group"
                            label="Address #:"
                            label-for="form-addressNum-input">
                    <b-form-input id="form-addressNum-input"
                                type="number"
                                v-model="form.addressNum"
                                required
                                placeholder="Enter address number:">
                    </b-form-input>
                </b-form-group>
                <b-form-group id="form-street-group"
                                label="Street:"
                                label-for="form-street-input">
                    <b-form-input id="form-street-input"
                                    type="text"
                                    v-model="form.street"
                                    required
                                    placeholder="Enter street:">
                    </b-form-input>
                </b-form-group>
                <b-form-group id="form-city-group"
                                label="City:"
                                label-for="form-city-input">
                    <b-form-input id="form-city-input"
                                    type="text"
                                    v-model="form.city"
                                    required
                                    placeholder="Enter city:">
                    </b-form-input>
                </b-form-group>
                <b-form-group id="form-state-group"
                                label="State:"
                                label-for="form-state-input">
                    <b-form-input id="form-state-input"
                                    type="text"
                                    v-model="form.state"
                                    required
                                    placeholder="Enter state:">
                    </b-form-input>
                </b-form-group>
                <b-form-group id="form-zipcode-group"
                                label="Zipcode:"
                                label-for="form-zipcode-input">
                    <b-form-input id="form-zipcode-input"
                                    type="number"
                                    v-model="form.zipcode"
                                    required
                                    placeholder="Enter zipcode:">
                    </b-form-input>
                </b-form-group>
                <b-form-group id="form-spotNumber-group"
                                label="Spot Number (Optional):"
                                label-for="form-spotNumber-input">
                    <b-form-input id="form-spotNumber-input"
                                    type="number"
                                    v-model="form.spotNumber"
                                    placeholder="Enter the spot's number (if applicable):">
                    </b-form-input>
                </b-form-group>
                <b-form-group id="form-price-group"
                                label="Price (per day):"
                                label-for="form-price-input">
                    <b-form-input id="form-price-input"
                                    type="number"
                                    v-model="form.price"
                                    required
                                    placeholder="Enter price for the spot per day:">
                    </b-form-input>
                </b-form-group>
                <b-button type="submit" variant="primary">Submit</b-button>
                <b-button type="reset" variant="danger">Reset</b-button>
            </b-form>
        </b-modal>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'ManageSpotsOwned',
    data() {
        return {
            form: {
                addressNum: '',
                street: '',
                city: '',
                state: '',
                zipcode: '',
                spotNumber: '',
                price: '',
            },
            spots: null,
            showError: false,
        }
    },
    methods: {
        connectAccount() {
            let userEmail = this.$store.getters.getEmail
            const path = `http://localhost:5000/connect/${userEmail}`
            axios.get(path).then((response) => {
                window.location = response.data.url
            })
        },
        getUserRegisteredSpots() {
            let userEmail = this.$store.getters.getEmail
            const path = `http://localhost:5000/spots/${userEmail}`
            axios.get(path).then((response) => {
                this.spots = response.data.spots
            })
        },
        addSpot(payload) {
            console.log(payload)
            const path = 'http://localhost:5000/spots';
            axios.post(path, payload).then((response) => {
                if (response.data.status == 'failed') { 
                    this.onReset();
                    this.showError = true;
                } else {
                    this.onReset()
                    this.$bvModal.hide('spot-modal')
                    this.getUserRegisteredSpots();
                }
            }).catch((error) => {
                console.log(error);
                this.$router.push("/")
            });
        },
        onSubmit() {
            const payload = {
                email: this.$store.getters.getEmail,
                addressNum: this.form.addressNum,
                street: this.form.street,
                city: this.form.city,
                state: this.form.state,
                zipcode: this.form.zipcode,
                spotNumber: this.form.spotNumber,
                price: this.form.price,
            };
            this.addSpot(payload);
        },
        onReset() {
            this.form.addressNum = ''
            this.form.street = ''
            this.form.city = ''
            this.form.state = ''
            this.form.zipcode = ''
            this.form.spotNumber = ''
            this.form.price = ''
        }
    },
    created: function() {
        this.getUserRegisteredSpots();
    }
}
</script>

<style scoped>
p {
  color: #0a814c;
  font-size: 2em;
}
</style>