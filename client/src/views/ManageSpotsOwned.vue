<template>
    <div id="manageSpotsOwned" class="container">
        <b-alert v-model="showError" variant="danger" dismissible>
            Failed to register spot!
        </b-alert>
        <div class="text-center">
            <p style="color: #0a814c; font-size: 2em;">Manage/Add Spots for Rent</p>
        </div>

        <span v-if="isConnected=='no'">
        <button type="button" class="btn btn-info btn-md" @click="connectAccount()">Connect with Stripe</button>
        <p style="margin-top: 10px;"><em>In order to list spots and get paid, please click the Connect with Stripe button above.<br> 
        All payments are processed through Stripe.<br>
        Please complete all steps.</em></p>
        </span>

        <span v-if="isConnected=='partly'">
        <button type="button" class="btn btn-warning btn-md" @click="connectAccount()">Finish Connecting</button>
        <p style="margin-top: 10px;"><em>You must finish onboarding with Stripe to be able to list spots and get paid.<br>
        Stripe does not require all information up front so this button may appear when Stripe needs more information.</em></p>
        </span>
        
        <span v-if="isConnected=='yes'">
        <button type="button" class="btn btn-success btn-md" v-b-modal.spot-modal>Add a New Spot for Rent</button>
        <button type="button" class="btn btn-primary btn-mid" style="margin-left: 10px;" @click="goToDashboard()">Go to Stripe Dashboard</button>
        <br>
        <br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Spot Address</th>
              <th scope='col'>Spot Number</th>
              <th scope="col">List Price</th>
              <th scope="col">Available Until</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="spot in spots" :key="spot.id">
              <td>{{spot.addressNum}} {{spot.street}}, {{spot.city}}, {{spot.state}} {{spot.zipcode}}</td>
              <td>{{spot.spotNumber}}</td>
              <td>${{spot.price}}/per day</td>
              <td>{{spot.available_until}}</td>
            </tr>
          </tbody>
        </table>
        </span>


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

                <b-form-group id="form-state-group" label="State:" label-for="form-state-input">
                    <b-form-select
                        id="form-state-input"
                        v-model="form.state"
                        :options="states"
                        required
                    ></b-form-select>
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
                <b-form-group id="form-date-group"
                                label="Available Until:"
                                label-for="form-date-input">
                    <b-form-input id="form-date-input"
                                    type="date"
                                    v-model="form.date"
                                    required>
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
                date: ''
            },
            spots: null,
            showError: false,
            states: ['Iowa']
        }
    },
    computed : {
        isConnected : function(){ return this.$store.getters.getConnection},
    },
    methods: {
        goToDashboard() {
            console.log('hello')
            let userEmail = this.$store.getters.getEmail
            const path = `http://localhost:5000/dashboard/${userEmail}`
            axios.get(path).then((response) => {
                window.location = response.data.url
            })
        },
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
                date: this.form.date
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
            this.form.date = ''
        }
    },
    created: function() {
        this.getUserRegisteredSpots();
    }
}
</script>

<style scoped>

</style>